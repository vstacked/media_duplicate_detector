import threading
import time
import PySimpleGUI as sg

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
            time.sleep(1)