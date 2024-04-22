from time import sleep
import threading
import PySimpleGUI as sg

def installation(window, steps):
    step = 1
    while step <= steps:
        window.write_event_value('JOB', f'Step {step} of Installation ...')
        sleep(1)
        step += 1
    window.write_event_value('JOB DONE', None)

def popup(message):
    sg.theme('DarkGrey')
    layout = [[sg.Text(message)]]
    window = sg.Window('Message', layout, no_titlebar=True, keep_on_top=True, finalize=True)
    return window

sg.theme('DarkBlue3')
sg.Window._move_all_windows = True

layout = [
    [sg.Button('Install', tooltip='Installation')],
    [sg.Text('', size=50, key='STATUS')],
]
window = sg.Window('Matplotlib', layout, finalize=True)
pop_win = None
while True:

    event, values = window.read(timeout=10)

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Install':
        window['Install'].update(disabled=True)
        popup_win = popup('Start installation...')
        window.force_focus()
        threading.Thread(target=installation, args=(window, 5), daemon=True).start()
    elif event == 'JOB':
        message = values['JOB']
        window['STATUS'].update(message)
    elif event == 'JOB DONE':
        popup_win.close()
        popup_win = None
        window['Install'].update(disabled=False)
        window['STATUS'].update("Installation done")

if popup_win:
    popup_win.close()
window.close()