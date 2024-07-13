import tkinter as tk
from tkinter import *

class RunDropDow:
    
    def __init__(self, root: Tk, menubar: tk.Menu) -> None:
        self.root = root
        self.menubar = menubar
        
    def create_dropdown(self, run_callback, step_callback, step_back_callback, pause_callback):
        '''Create the run menu'''
        
        run_menu = tk.Menu(self.menubar, tearoff=False)
        run_menu.add_command(
            label= 'Run',
            accelerator= 'F5',
            command= run_callback
        )
        run_menu.add_command(
            label= 'Step',
            accelerator= 'F10',
            command= step_callback
        )
        run_menu.add_command(
            label= 'Step Back',
            accelerator= 'F11',
            command= step_back_callback
        )
        run_menu.add_command(
            label= 'Pause',
            accelerator= 'F12',
            command= pause_callback
        )
        
        self.root.bind_all("<F5>", run_callback)
        self.root.bind_all("<F10>", step_callback)
        self.root.bind_all("<F11>", step_back_callback)
        self.root.bind_all("<F12>", pause_callback)
        self.menubar.add_cascade(menu=run_menu, label='Run')
        
        self.root.config(menu=self.menubar)