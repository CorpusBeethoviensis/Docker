import os
import io
import multiprocessing
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk, messagebox
import musicdiff
from pathlib import Path
import sys


""" class DirectorySelector(tk.Tk):
        def __init__(self,):
        super().__init__()
        self.main_directory = None
        self.output_dir = None

        self.withdraw()
        self.title('Selection for comparison')

        main_directory_button = ttk.Button(self, text="Select a directory with mei-files", command=self.select_main_directorie)
        main_directory_button.pack(expand=True)

        output_dir_button = ttk.Button(self, text="Select a directory to save results", command=self.select_out_dir)
        output_dir_button.pack(expand=True)

        submit_button = ttk.Button(self, text="Submit", command=self.submit) 
        submit_button.pack(expand=True)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.setup_ui(self)

def setup_ui(self, window):
        window_width = 300
        window_height = 200 
        #  get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def select_main_directorie(self):
        self.main_directory= fd.askdirectory(title="Select a directory (Cancel to finish)") 
        

    def select_out_dir(self):
        self.output_dir = fd.askdirectory(title="Select output directory")
        if self.main_directory and self.output_dir:
            print(f'You selected {self.main_directory} with mei-files and {self.output_dir} to save the comparison-results to.')

    def submit(self):
        if self.main_directory and self.output_dir:
            print('Oops, you did it again! Closing window now.')
            self.quit()
            self.destroy()
        else:
            print(f"You're not done yet. Finish the job!")

    def on_closing(self):
        self.quit()
        self.destroy() """

    
""" def select_directories_window(): 
    selector = DirectorySelector() 
    selector.deiconify() # Zeigt das Fenster an 
    selector.mainloop() # Startet die Hauptschleife 


    return selector.main_directory, selector.output_dir """

    
        

def compare_files_in_directories(main_directory, output_dir): 
    subdirs = sorted(os.listdir(main_directory))
    #tasks = []

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
    """ with multiprocessing.Pool() as pool:
        pool.starmap(compare_files, tasks) """
                    

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


""" def compare_all_files(base_dirs, output_dir, file_extension):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Annahme: Alle Ordner haben die gleiche Anzahl an Dateien und die Dateien sind in der gleichen Reihenfolge sortiert
    files_in_dirs = [sorted([f for f in os.listdir(base_dir) if f.endswith(file_extension)]) for base_dir in base_dirs]
    num_files = min(len(files) for files in files_in_dirs)  # Anzahl der Dateien im kleinsten Ordner

    for i in range(num_files):
        for j in range(len(base_dirs)):
            for k in range(j + 1, len(base_dirs)): 
                file1 = os.path.join(base_dirs[j], files_in_dirs[j][i]) 
                file2 = os.path.join(base_dirs[k], files_in_dirs[k][i])  """