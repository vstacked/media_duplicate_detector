import PySimpleGUI as sg
import os.path
import detect8
from collapsible import Collapsible
from collections import OrderedDict
import re

KEY_FOLDER = "-FOLDER-"
KEY_FILE_LIST = "-FILE LIST-"
KEY_PROCESS = "-PROCESS-"
KEY_SETTINGS = "-SETTINGS-"
KEY_OUTPUT = "-OUTPUT-"
KEY_INPUT_EXTENSION = "-INPUT EXTENSION-"
KEY_BUTTON_EXTENSION = "-BUTTON EXTENSION-"
KEY_REMOVE_ALL_EXTENSION = "-REMOVE ALL EXTENSION-"
KEY_EXTENSIONS_LIST = "-EXTENSIONS LIST-"
KEY_CHECKBOX_EXTENSIONS = "-CHECKBOX EXTENSIONS-"
KEY_TITLE_EXTENSION ="-TITLE EXTENSION-"

file_extensions = (".jpg", ".jpeg", ".png", ".gif", ".mp4", ".mkv", ".docx", ".pdf", ".pptx", ".txt")

def update_file_list():
    folder = values[KEY_FOLDER]
    try:
        # Get list of files in the folder
        file_list = os.listdir(folder)
    except:
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith(file_extensions)
    ]
    window[KEY_FILE_LIST].update(fnames)
    if fnames:
        window[KEY_PROCESS].update(disabled=False)
    else:
        window[KEY_PROCESS].update(disabled=True)

def filter_file_extensions(split_values):
    new_values = []
    for val in split_values:
        val = str(val).strip();

        """
        Checks if a text string is valid based on the criteria:
        - Starts with a dot (.)
        - Contains only lowercase (a-z), uppercase (A-Z), or numbers (0-9) afterwards
        """
        pattern = r"^\.[a-zA-Z0-9]+$"  # Regular expression pattern
        match = bool(re.match(pattern, val))

        if bool(match):
            new_values.append(val)
    return new_values;

sg.theme('GreenTan')

settings = [
    [sg.Text(text="Add New Extension(s) [e.g., .txt, .jpg]:",key=KEY_TITLE_EXTENSION)],
    [
        sg.Input(key=KEY_INPUT_EXTENSION),
        sg.Button(button_text="Add", key=KEY_BUTTON_EXTENSION, bind_return_key=True),
        sg.Button(button_text="Remove All", key=KEY_REMOVE_ALL_EXTENSION,visible=False),
    ],
    [sg.Multiline((f"{', '.join(file_extensions)}"), key=KEY_EXTENSIONS_LIST, size=(70, 3), disabled=True)],
    [sg.Checkbox("Remove Selected Extension(s)", key=KEY_CHECKBOX_EXTENSIONS, enable_events=True)]
]

file_list_column = [
    [
        sg.Text("Media Folder"),
        sg.In(size=(25, 1), enable_events=True, disabled=True, key=KEY_FOLDER),
        sg.FolderBrowse(),
    ],
    [sg.Listbox(values=[], enable_events=False, size=(70, 10), pad=(25,0), key=KEY_FILE_LIST)],
    [sg.Button(button_text="Process",key=KEY_PROCESS, size=(63, 1), pad=(25,0), disabled=True)],
    [sg.Output(size=(70, 10), key=KEY_OUTPUT, pad=(25,20))],
    [sg.HorizontalSeparator()],
    [Collapsible(settings, KEY_SETTINGS, 'Advanced Settings', collapsed=True)],
]

# ----- Full layout -----
layout = [
    [sg.Column(file_list_column)]
]

window = sg.Window("Media Detector", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # Folder name was filled in, make a list of files in the folder
    if event.startswith(KEY_FOLDER):
        update_file_list()

    elif event.startswith(KEY_PROCESS):
        window[KEY_PROCESS].update(disabled=True)
        result = detect8.main(values[KEY_FOLDER], file_extensions)
        if(result == True):
            window[KEY_PROCESS].update(disabled=False)
            update_file_list()

    elif event.startswith(KEY_SETTINGS):
        window[KEY_SETTINGS].update(visible=not window[KEY_SETTINGS].visible)
        window[KEY_SETTINGS+'-BUTTON-'].update(
            window[KEY_SETTINGS].metadata[0] if window[KEY_SETTINGS].visible
            else window[KEY_SETTINGS].metadata[1]
        )

    elif event.startswith(KEY_BUTTON_EXTENSION):
        if values[KEY_INPUT_EXTENSION]:
            split_values = values[KEY_INPUT_EXTENSION].split(",")
            filtered = filter_file_extensions(split_values)

            if values[KEY_CHECKBOX_EXTENSIONS]:
                upd = list(file_extensions)
                for val in filtered:
                    if val in upd:
                        upd.remove(val)
                file_extensions = tuple(upd)
            else:
                upd = file_extensions + tuple(filtered)
                # Removing duplicates from tuple 
                file_extensions = tuple(OrderedDict.fromkeys(upd).keys())

            window[KEY_EXTENSIONS_LIST].Update(f"{', '.join(file_extensions)}")
            window[KEY_INPUT_EXTENSION].update("")
            update_file_list()

    elif event.startswith(KEY_CHECKBOX_EXTENSIONS):
        val = values[KEY_CHECKBOX_EXTENSIONS]
        window[KEY_TITLE_EXTENSION].update(
            "Remove Extension(s) [e.g., .txt, .jpg]:" if val
            else "Add New Extension(s) [e.g., .txt, .jpg]:"
        )
        window[KEY_BUTTON_EXTENSION].update("Remove" if val else "Add")
        window[KEY_REMOVE_ALL_EXTENSION].update(visible=val)

    elif event.startswith(KEY_REMOVE_ALL_EXTENSION):
        file_extensions = tuple([])

        window[KEY_EXTENSIONS_LIST].Update(f"{', '.join(file_extensions)}")
        window[KEY_INPUT_EXTENSION].update("")
        update_file_list()


window.close()
