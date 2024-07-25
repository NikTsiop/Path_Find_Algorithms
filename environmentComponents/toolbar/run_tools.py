import sys
import os

# Append the root directory to sys.path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, root_path)  # Insert at the beginning of sys.path

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from config import AlgorithmsTypes

ICONS_PATH = './assets/icons/'

class RunToolbar:
    
    def __init__(self, root, run_config) -> None:
        self.root = root
        self.run_config = run_config
    
    def validation_entry(text, new_text):
        # First check that the entire content has no more than ten characters.
        if len(new_text) > 5:
            return False
        # Then make sure the text is numeric-only.
        return text.isdecimal()
    
    def selection_changed(self, event):
        algorithms = event.widget
        selected_value = algorithms.get()
        self.run_config.algorithm = AlgorithmsTypes[selected_value].value
    
    def update(self, event):
        widget = event.widget
        widget.master.focus_set()
        value = widget.get()
        self.run_config.update_config(step_delay =value)
    
    def create_run_config_menu(self, run_callback, step_back_callback, step_callback, clear_steps, clear_grid):
        '''Run configuration menu'''
        run_config_menu = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        
        play_original_image = Image.open(rf"{ICONS_PATH}play.png")
        play_icon_image = ImageTk.PhotoImage(play_original_image.resize((16, 16)))
        play_button = tk.Button(run_config_menu, image=play_icon_image, command= run_callback)
        play_button.image = play_icon_image      
        play_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        back_step_original_image = Image.open(rf"{ICONS_PATH}back_step.png")
        back_step_icon_image = ImageTk.PhotoImage(back_step_original_image.resize((16, 16)))
        back_step_button = tk.Button(run_config_menu, image=back_step_icon_image, command= step_back_callback)
        back_step_button.image = back_step_icon_image      
        back_step_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        step_original_image = Image.open(rf"{ICONS_PATH}step.png")
        step_icon_image = ImageTk.PhotoImage(step_original_image.resize((16, 16)))
        step_button = tk.Button(run_config_menu, image=step_icon_image, command= step_callback)
        step_button.image = step_icon_image      
        step_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        reset_original_image = Image.open(rf"{ICONS_PATH}reset.png")
        reset_icon_image = ImageTk.PhotoImage(reset_original_image.resize((16, 16)))
        reset_button = tk.Button(run_config_menu, image=reset_icon_image, command= clear_steps)
        reset_button.image = reset_icon_image      
        reset_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        clear_original_image = Image.open(rf"{ICONS_PATH}clear.png")
        clear_icon_image = ImageTk.PhotoImage(clear_original_image.resize((16, 16)))
        clear_button = tk.Button(run_config_menu, image=clear_icon_image, command= clear_grid)
        clear_button.image = clear_icon_image      
        clear_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        #Combobox for choosing of argolirthms
        algorithms_dropdown = ttk.Combobox(
            run_config_menu,
            state="readonly",
            values= ['DFS', 'BFS'] #TODO replace with dynamic 
        )
        algorithms_dropdown.current(self.run_config.algorithm.value)
        algorithms_dropdown.pack(side=tk.LEFT, padx=2, pady=2)
        algorithms_dropdown.bind("<<ComboboxSelected>>", self.selection_changed)
        
        show_full_search_val = tk.BooleanVar()
        show_full_search = tk.Checkbutton(
            run_config_menu, 
            text='Show full search', 
            variable=show_full_search_val,
            command=lambda: self.run_config.update_config(full_solution = str(show_full_search_val.get()))
        )
        show_full_search.pack(side=tk.LEFT, padx=2, pady=2)
        
        step_delay_var = tk.StringVar()
        step_delay_var.set(self.run_config.step_delay)
        step_delay_label= tk.Label(run_config_menu, text='Step Delay', font=('caribre', 10, 'bold'))
        step_delay_label.pack(side=tk.LEFT, padx=2, pady=2)
        step_delay_entry = tk.Entry(
            run_config_menu, 
            textvariable=step_delay_var, 
            font=('calibre', 10, 'normal'),
            width=5, 
            validatecommand=(run_config_menu.register(self.validation_entry), "%S", "%P")
        )
        step_delay_entry.pack(side=tk.LEFT, padx=2, pady=2)
        #step_delay_entry.bind("<Return>", lambda event: self.run_config.update_config(step_delay = step_delay_entry.get()))
        step_delay_entry.bind("<Return>", self.update)  
        
        run_config_menu.grid(row=0, column=0, sticky='nsew')
        
        self.root.grid_columnconfigure(0, weight=1)
        
        self.root.update_idletasks()
        width = run_config_menu.winfo_reqwidth()
        height = run_config_menu.winfo_reqheight()
        self.root.geometry(f"{width}x{height}")