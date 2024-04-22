import PySimpleGUI as sg
import time
import threading

test_worker = False

class SimpleWorker : 
    def __init__(self, window : sg.Window) :
        # INIT Worker's variable
        self.run = False
        self.window = window
        
    def start_thread(self) :
        # Only Do something if not running
        if not self.run :
            # Create Thread from job_processing function
            self.job_threading = threading.Thread(target=self.job_processing)
            self.job_threading.start()
    
    def stop_thread(self) :
        # Tell Worker to stop
        self.run = False

    def job_processing(self) :
        # Set to run
        self.run = True
        while self.run :
            ## 1: Get Data From Local SHARED DB
            ## 2: DO SOMETHING
            ## 3: Update/Insert Result to Local SHARED DB
            ## 4: Delay ## Optional

            # name = self.values["name"]
            # age = self.values["age"]
            # message = f'Hello, {name}! You are {age} years old.'
            # # Display Result
            if test_worker:
                time.sleep(3)
                self.window['result'].update("test")

            time.sleep(1)

# Define the layout of the GUI
layout = [
    [sg.Text('What is your name?'), sg.InputText(key= 'name')],
    [sg.Text('What is your age?'), sg.InputText(key= 'age')],
    [sg.Button('Submit'), sg.Button('Cancel')],
    [sg.Text('', text_color='red', background_color='yellow', key= 'result')]
]

# Create the GUI window
window = sg.Window('My Simple App', layout)
# Create and Start Worker
worker = SimpleWorker(window= window)
worker.start_thread()


# Event loop to process user input
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        worker.stop_thread()
        break
    elif event == 'Submit' :
        test_worker=True
        name = values["name"]
        age = values["age"]
        message = f'Hello, {name}! You are {age} years old.'
        # Display Result
        # window['result'].update(message)

# Close the GUI window
window.close()
#If we run this code and submit “name” and “age”, the GUI will freeze for 10 seconds. because the GUI needs to wait for 30 seconds before moving to the next stage.