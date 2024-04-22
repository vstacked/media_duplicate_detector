import PySimpleGUI as sg
import os.path
import detect8

def update_file_list():
    folder = values["-FOLDER-"]
    try:
        # Get list of files in the folder
        file_list = os.listdir(folder)
    except:
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith(
            (".jpg", ".jpeg", ".png", ".gif", ".JPG", ".mp4", ".mkv", ".MP4", ".docx", ".pdf", ".pptx", ".txt")
        )
    ]
    window["-FILE LIST-"].update(fnames)
    if fnames:
        window["Process"].update(disabled=False)
    else:
        window["Process"].update(disabled=True)

# First the window layout in 2 columns

sg.theme('GreenTan')

file_list_column = [
    [
        sg.Text("Media Folder"),
        sg.In(size=(25, 1), enable_events=True, disabled=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [sg.Listbox(values=[], enable_events=False, size=(70, 10), pad=(25,0), key="-FILE LIST-")],
    [sg.Button("Process", size=(63, 1), pad=(25,0), disabled=True)],
    [sg.Output(size=(70, 10), key="-OUTPUT-", pad=(25,20))]
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        # sg.VSeperator(),
        # sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Media Detector", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        update_file_list()

    elif event == "Process":
        window["Process"].update(disabled=True)
        result = detect8.main(values["-FOLDER-"])
        if(result == True):
            window["Process"].update(disabled=False)
            update_file_list()

    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0]).replace("\\", "/")
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass

window.close()
