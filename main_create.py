import tkinter as tk
import os
from tkinter import StringVar
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo
from parse_file import parse_file
from create_file import make_file, copy_until_measure
from selection_algorithms import random_selection, measures_elements, only_elements

""" class FileCreation: """
""" def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.measures = None
        self.selected_measures = []
        self.filename = None
        self.select_file_window()

    def setup_ui(self, window):
        window_width = 300
        window_height = 200 
        #  get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def on_close(self, window):
        Beendet das Programm, wenn das Fenster geschlossen wird
        result = messagebox.askokcancel("Quit", "Do you really want to exit? This will end the program.")
        if result:
            window.destroy()
            self.root.quit() """

""" def select_file_window(self):
        file_window = tk.Toplevel(self.root)
        file_window.title("Select a file")

        self.setup_ui(file_window)

        directory_button = ttk.Button(file_window, text="Select a local file", command=lambda: self.select_file(file_window))
        directory_button.pack(expand=True)

        file_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close(file_window))
 """

""" def select_file(self, window):
        self.filename = fd.askopenfilename()
        if self.filename is None:
            print("Please select a file.")
        if self.filename:
            print("Selected file:", self.filename)
            self.measures = parse_file(self.filename)
            window.destroy()
            self.select_algorithm_window()
            return self.measures """
    
""" def select_algorithm_window(self):
        algo_window = tk.Toplevel(self.root)
        algo_window.title("Select an algorithm")

        self.setup_ui(algo_window)

        algorithms = ["Select algorithm", "Random", "Bars and Elements", "Elements"]
        self.data_type = StringVar(algo_window)
        self.data_type.set("Select algorithm")

        selection_dropdown = ttk.OptionMenu(algo_window, self.data_type, *algorithms)
        selection_dropdown.pack(expand=True)

        selection_button = ttk.Button(algo_window, text="Select", command=lambda: self.select(algo_window))
        selection_button.pack(expand=True)

        algo_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close(algo_window)) """

def select(measures, directory):
        if measures is None:
            print("Please selecte a file first")
            return
        print("Select one of the following algorithms to choose measures from your MEI-file:")
        print("1: Completely random selection of 10{%} of the measures.")
        print("2: Select 10{%} of the meausres including 10{%} of all elements.")
        print("3: Select arbitrary number of measures containing 10{%} of all elements.")
        selected_algorithm = input("Chose 1, 2 or 3: ")
        print("Gewählter Algorithmus:", selected_algorithm)
        number_of_samples = int(input("How many samples do you need? "))
        sample_size = input("How many measures should be sampled? ").strip() or None
        if sample_size is not None:
            sample_size = int(sample_size)
        
            if sample_size < 0 or number_of_samples < 0:
                print(f'Number of samples or size of the sample must be a positive value.')
                return
            if number_of_samples == 0 or sample_size == 0:
                print(f'Number of samples or size of the sample too small.')
                return
            print(f'Number of Samples: {number_of_samples}')
        base_directory = input("Enter the directory where the files should be saved: ").strip()
    
        # Falls keine Eingabe erfolgt, Standardwert setzen (z. B. `main_directory`)
        if not base_directory:
            base_directory = main_directory  

        # Sicherstellen, dass das Verzeichnis existiert
        os.makedirs(base_directory, exist_ok=True)
            
        for i in range(number_of_samples):
            short_algo = None
            if selected_algorithm == "Select algorithm":
                print("Please select an algorithm")
            elif selected_algorithm == "1":
                short_algo = "rm"
                selected_measures, state = random_selection(measures, sample_size = None)
            elif selected_algorithm == "2":
                short_algo = "mue"
                selected_measures, state = measures_elements(measures, sample_size = None)
            else:
                short_algo = "elem"
                selected_measures, state = only_elements(measures)
        
            if selected_measures and state:
                print("Selected measures:", selected_measures)
                create_file(selected_measures, directory, base_directory, i, state, short_algo)

""" def create_file_window(self):
        create_window = tk.Toplevel(self.root)
        create_window.title("Create new file")

        self.setup_ui(create_window)

        make_file_button = ttk.Button(create_window, text="Create file with selected measures", command=lambda: self.create_file(create_window))
        make_file_button.pack(expand=True)

        create_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close(create_window))
 """
def create_file(selected_measures, directory, base_directory, i, state, short_algo):
        print(sorted(selected_measures))
        if selected_measures is not None and directory is not None:
            make_file(selected_measures, directory, base_directory, i, state, short_algo)
            

def ask_other_file(selected_measures):
        response = input("Would you like to copy the measures from another file, too (y/n)?")
        if response == "y":
            filename = input("Please select the MEI-file: ")
            if filename:
                create_file(selected_measures, filename)
                ask_other_file(selected_measures)
        else:
            ask_new_file()

def ask_new_file():
        response = input("Would you like to select measures from another file (y/n)?")
        if response == "y":
            main()
        else:
            return



def main():
    """ root = tk.Tk()
    app = FileCreation(root) """
    filename = input("Select MEI-file to copy measures from: ")
    directory = input("Select directory with MEI-files to copy measures from.")
    if filename:
            print("Selected file:", filename)
            measures = parse_file(filename)
            selected_measures = select(measures, directory)
            """ if selected_measures:
                create_file(selected_measures, directory)
                ask_other_file(selected_measures) """
            
    """ root.mainloop() """

if __name__ == "main":
    main()