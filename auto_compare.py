import os
import io
import multiprocessing
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk, messagebox
import musicdiff
from pathlib import Path
import sys


def compare_files_in_directories(main_directory, output_dir): 
    subdirs = sorted(os.listdir(main_directory))

    for subdir in subdirs: 
        full_subdir_path = os.path.join(main_directory, subdir) 
        if os.path.isdir(full_subdir_path): 
            files = sorted([f for f in os.listdir(full_subdir_path) if f.endswith('.mei')]) 
            
            for i in range(len(files)): 
                for j in range(i + 1, len(files)): 
                    file1 = os.path.join(full_subdir_path, files[i]) 
                    file2 = os.path.join(full_subdir_path, files[j])

                    new_output_dir = os.path.join(output_dir, f"{subdir}_result") 
                    os.makedirs(new_output_dir, exist_ok=True)

                    output_file = os.path.join(new_output_dir, f"{os.path.basename(file1)}_{os.path.basename(file2)}.txt") 
                    #tasks.append((file1, file2, output_file))
                    compare_files(file1, file2, output_file)


def compare_files(file1, file2, output_file):
    print(file1, file2)
    output = io.StringIO()
    visualize = False  # Setze auf True, falls eine visuelle Ausgabe gewünscht ist
    text_out = True  # Setze auf False, falls keine Textausgabe gewünscht ist
    detail = musicdiff.detaillevel.DetailLevel.DecoratedNotesAndRests|musicdiff.detaillevel.DetailLevel.AllObjects|musicdiff.detaillevel.DetailLevel.NotesAndRests|musicdiff.detaillevel.DetailLevel.Beams|musicdiff.detaillevel.DetailLevel.Tremolos|musicdiff.detaillevel.DetailLevel.Ornaments|musicdiff.detaillevel.DetailLevel.Articulations|musicdiff.detaillevel.DetailLevel.Ties|musicdiff.detaillevel.DetailLevel.Slurs|musicdiff.detaillevel.DetailLevel.Signatures|musicdiff.detaillevel.DetailLevel.Directions|musicdiff.detaillevel.DetailLevel.Barlines|musicdiff.detaillevel.DetailLevel.StaffDetails|musicdiff.detaillevel.DetailLevel.ChordSymbols|musicdiff.detaillevel.DetailLevel.Ottavas|musicdiff.detaillevel.DetailLevel.Arpeggios|musicdiff.detaillevel.DetailLevel.Lyrics|musicdiff.detaillevel.DetailLevel.Style|musicdiff.detaillevel.DetailLevel.Voicing      # Detaillevel einstellen

    try:
        sys.stdout = output
        musicdiff.diff(score1=file1, score2=file2, visualize_diffs=visualize, print_text_output=text_out, detail=detail)
        
        
        with open(output_file, "w") as file:
            file.write(output.getvalue())
        output.close()

    except IndexError as e:
        print(f'Index error: {e}')

    except FileNotFoundError:
        print(f"Error during comparison: {file1} or {file2} not found")

    finally:
        sys.stdout = sys.__stdout__



# In der Funktion musicdiff.diff den Aufruf von get_text_output anpassen


def main(): 
    main_directory = input("Select directory with MEI-files to compare: ")
    output_dir = input("Select a directory to safe the txt-result-files to")
    if main_directory and output_dir: 
        compare_files_in_directories(main_directory, output_dir) 
    else: print("Please select all required directories.")

if __name__ == "__main__":
    main()
