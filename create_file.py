import xml.etree.ElementTree as ET
from tkinter import filedialog as fd
import os
from pathlib import Path

def save_file(tree, filename):
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)
    tree_str = ET.tostring(tree.getroot(), encoding='utf-8', method='xml')
    with open(filename, 'wb') as f:
        f.write(tree_str)
        print(f"Die Datei wurde unter {filename} gespeichert.")

def copy_until_measure(elem, parent, selected_measures, ns):
    new_elem = ET.SubElement(parent, elem.tag, attrib=elem.attrib)

    if elem.text:
        new_elem.text = elem.text
            
    for child in elem:
        if child.tag.endswith('measure'):
            n = int(child.attrib.get('n'))
            if n not in selected_measures:
                continue
        if child.tag.endswith('sb') or child.tag.endswith('pb'):
            continue
        copy_until_measure(child, new_elem, selected_measures, ns)
        

    return parent

def make_file(selected_measures,  main_directory, base_directory, i, state, short_algo):
    files = sorted([f for f in os.listdir(main_directory) if f.endswith('.mei')])
    print(files)
    

    # Erstelle das neue Unterverzeichnis innerhalb des gewählten Speicherorts
    new_directory = os.path.join(base_directory, f"samples_{i}")
    os.makedirs(new_directory, exist_ok=True)
    state_file = os.path.join(new_directory, f"state_file_{i}")
    with open (state_file, 'w') as f:
        f.write(str(state))
    

    for file in files:
        new_file = os.path.join(new_directory, f"{os.path.splitext(file)[0]}_{short_algo}.mei")
        filename = os.path.join(main_directory, file)

        tree = ET.parse(filename)
        root = tree.getroot()

        ns = {"mei": "http://www.music-encoding.org/ns/mei"}
        ET.register_namespace('', ns["mei"])

        new_root = ET.Element('mei', attrib={'meiversion': '5.0'})

        for child in root:
            copy_until_measure(child, new_root, selected_measures, ns)

        #filename = input("Please enter a directory incl. name for the new file (Must end with .mei): ")
        """ fd.asksaveasfilename(defaultextension=".mei",
                                            filetypes=[("MEI files", "*.mei")]) """

        # Speichere das neue Dokument
        new_tree = ET.ElementTree(new_root)
        save_file(new_tree, new_file)