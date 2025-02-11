import xml.etree.ElementTree as ET
from tkinter import filedialog as fd
element_list = ('note', 'rest', 'chord', 'slur', 'dynam', 'tie', 'accid', 'beam', 'clef', 
                'tempo', 'artic', 'fermata', 'dir', 'tuplet', 'keySig', 'meterSig')


def parse_file(filename):
        file = open(filename, "r") 
        tree = ET.parse(file)
        root = tree.getroot()
#   print(root)
        elements: dict[str, int] = {}                    #leeres Dictionary, dass die Elemente und ihre Anzahl enthalten wird
        measures: dict[str, int]= {}                       #leeres Dictionary, dass die Taktzahlen und die Zahl an in ihnen enthaltenen Elementen enthalten wird.
        for element in root.iter():         #iteriert über den ganzen Baum und findet alle Elemente
            tag_list = element.tag.split('}')   #Teilt den Elementnamen in den Namespace und das Tag auf
            tag = tag_list[-1]                      #wählt das Tag aus
            if tag in element_list:             #überprüft, ob das Tag in element_list enthalten sit
            #print(tag)
                if tag in elements:                     #prüft, ob dass tag schon im dictionary elements enthalten ist
                    elements.update({tag: str(int(elements[tag]) + 1)})         #aktualisiert den Eintrag
                else:
                    elements.update({tag: 1})               #fügt einen neuen Eintrag hinzu  
        #print(elements)
        for measure in root.iter('{http://www.music-encoding.org/ns/mei}measure'):              #findet alle measure-elemente
            n = measure.get('n')                 #sucht die n-Attribute der measure elemente
            measures.update({n: 0})              #updated das dictionary
            for element in measure.iter():              #iteriert über alle Kindelemente
                tag_list = element.tag.split('}') 
                tag = tag_list[-1]
            #print(tag)
                if tag in element_list:
                #print(tag)
                    measures.update({n: measures[n]+1})
                #count = count + 1
        #measures.update({n : count})
        print((measures), "Summe:", sum(measures.values()))
    
        """ for m in range(0, len(measures)):
            m1 = '{}'.format(m)
            try:
                print(f' Takt {m} enthält {measures[m1]} Elemente')
            except KeyError:
                print("Keinen Eintrag für gefunden für:", m) """
        return(measures)

if __name__ == "__main__":
    measures = parse_file()
    print(type(measures))
