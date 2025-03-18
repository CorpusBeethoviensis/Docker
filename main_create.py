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

def select(measures, directory, number_of_samples):

        algorithms = [1, 2, 3]
        for n in range(0, 3):
            selected_algorithm = algorithms[n]
            
            for i in range(number_of_samples):
                short_algo = None
                if selected_algorithm == algorithms[0]:
                    print('Random selection!')
                    short_algo = "rm"
                    base_directory = os.path.join(directory, short_algo)
                    os.makedirs(base_directory, exist_ok=True)
                    selected_measures, state = random_selection(measures, sample_size = None)
                elif selected_algorithm == algorithms[1]:
                    print('Measures and elements!')
                    short_algo = "mue"
                    base_directory = os.path.join(directory, short_algo)
                    os.makedirs(base_directory, exist_ok=True)
                    selected_measures, state = measures_elements(measures, sample_size = None)
                else:
                    print('Only elements!')
                    short_algo = "elem"
                    base_directory = os.path.join(directory, short_algo)
                    os.makedirs(base_directory, exist_ok=True)
                    selected_measures, state = only_elements(measures)
            
                if selected_measures and state:
                    print("Selected measures:", selected_measures)
                    create_file(selected_measures, directory, base_directory, i, state, short_algo)


def create_file(selected_measures, directory, base_directory, i, state, short_algo):
        print(sorted(selected_measures), directory, base_directory)
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



def main(main_directory):


    number_of_samples = int(input("How many samples do you need?"))
    
    for dir in sorted(os.listdir(main_directory)):
        full_path = os.path.join(main_directory, dir)
        if os.path.isdir(full_path):
            try:
                files = os.listdir(full_path)
                for f in files:
                    if f.startswith('1803_BdA'):
                        filename = os.path.join(full_path, f)
                        if filename:
                            print("Selected file:", filename)
                            measures = parse_file(filename)
                            selected_measures = select(measures, full_path, number_of_samples)
                        else:
                            print('No file found')
                    else:
                        pass
            except Exception as e:
                print(f'Fail: Exception {e}')

                      
                                

if __name__ == "main":
    main()
