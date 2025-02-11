import random as rm
import numpy as np
from termcolor import colored


def random_selection(measures, sample_size = None):
    if sample_size is not None:
        if sample_size >= len(measures):
            print(f"Error: Fuck you I'm not Beethoven. Only {len{measures}} Measures in the piece.")
        else:
            required_measures = sample_size
    else:
         required_measures = int(np.ceil(len(measures) * 0.1))
    valid_measures = [int(key) for key in measures.keys() if key is not None]
    print(valid_measures)
    state = rm.getstate()
    selection = sorted(rm.sample(valid_measures, required_measures))
    print("Zahl auszuwählender Takte:", required_measures)
    print(selection)
    return selection, state

#random_selection()

def measures_elements(measures, sample_size = None):
    measure_selection = []  #leere Liste, in der die ausgewählten Takte gespeichert werden sollen
    selected_elements = []  #leere Liste, in der die Zahl an enthaltenen Elemente gespeichert werden sollen
    available_measures = [int(key) for key in measures.keys()]     #Liste mit noch nicht ausgewählten Takten
    if sample_size is not None:
        if sample_size >= len(measures):
            print(f"Error: Fuck you I'm not Beethoven. Only {len{measures}} Measures in the piece."}
        else:
            required_measures = sample_size
    else:
        required_measures = int(np.ceil(len(measures) * 0.1))   #berechnet die Zahl benötigter Takte
    measure_ratio = required_measures / len(measures)
    required_elements = int(np.ceil(sum(measures.values()) * measure_ratio))    #berechnet die Zahl benötigter Elemente
    max_attempts = len(measures)
    attempts = 0
    upper_bound = required_elements * 1.05
    lower_bound = required_elements * 0.95
    print(required_measures, required_elements)
    current_sum = sum(selected_elements)
    state = rm.getstate()
    while len(measure_selection) != required_measures or current_sum < lower_bound:
            x = rm.choice(available_measures)   #wählt einen Takt aus
            measure_selection.append(x)
            available_measures.remove(x)
            selected_elements.append(measures[str(x)])
            current_sum = sum(selected_elements)
            print(f"Takt {x}, Summe {current_sum}")
            if len(measure_selection) > required_measures:
                    r = rm.choice(measure_selection)
                    e = measures[str(r)]
                    measure_selection.remove(r)
                    selected_elements.remove(e)
                    current_sum = sum(selected_elements)
                    print(f"Die maximale Zahl an Takten wurde überschritten, Takt {r} und {e} Elemente entfernt")
            while current_sum > upper_bound:                                #falls ja, wird er wieder entfernt
                    r = rm.choice(measure_selection)
                    e = measures[str(r)]
                    measure_selection.remove(r)
                    selected_elements.remove(e)
                    current_sum = sum(selected_elements)
                    print(f"Die obere Grenze wurde überschritten, Takt {r} und {e} Elemente entfernt." )

            attempts += 1
            if attempts == max_attempts:
                 print("Maximale Zahl an Versuchen erreicht. Es konnten keine bessere Lösung gefunden werden.")
                 break                 
                
    if current_sum < lower_bound:
         print(colored("Warnung: Die erreichte Summe liegt unterhalb der unteren Grenze:", "red"), current_sum, lower_bound)
    elif current_sum > upper_bound:
         print(colored("Warnung: Die erreichte Summe liegt oberhalb der oberen Grenze:", "red"), current_sum, upper_bound)
    else:
         print(colored("Die Summe liegt innerhalb der Grenzen:", "green"), current_sum, lower_bound, upper_bound)

    print("Ausgewählte Takte:", sorted(measure_selection), "Gesamt:", len(measure_selection), "Elemente:", selected_elements,
           "Gesamt:", sum(selected_elements), "upper bound:", upper_bound, "lower bound:", lower_bound, attempts)
    return sorted(measure_selection), state


#measures_elements()

def only_elements(measures):
     state = rm.getstate()
     measure_selection = []
     selected_elements = []
     available_measures = [int(key) for key in measures.keys()]
     z = int(np.ceil(sum(measures.values()) * 0.1))
     max_attempts = len(measures)
     attempts = 0
     print("Auszuwählende Zahl an Elementen:", z)
     current_sum = sum(selected_elements)
     upper_bound = z * 1.05
     lower_bound = z * 0.95
     while current_sum <= lower_bound and attempts < max_attempts:
        x = rm.choice(available_measures)   #wählt einen Takt aus
        print("Takt:", x)
        measure_selection.append(x)
        selected_elements.append(measures[str(x)])
            #print(measure_selection, selected_elements)
        current_sum = sum(selected_elements)
        attempts += 1
        print("Aktuelle Summe:", current_sum)
        while current_sum > upper_bound:
                r = rm.choice(measure_selection)
                e = measures[str(r)]
                measure_selection.remove(r)
                selected_elements.remove(e)
                current_sum = sum(selected_elements)
                print(f"Die Summe überschreitet die obere Grenze, Takt {r} entfernt")
        else:
            available_measures.remove(x)
        if attempts == max_attempts:
            print("Maximale Zahl an Versuchen erreicht. Es konnte keine bessere Lösung gefunden werden.")
        sorted_selection = sorted(measure_selection)
     if current_sum < lower_bound:
         print(colored("Warnung: Die erreichte Summe liegt unterhalb der unteren Grenze:", "red"), current_sum, lower_bound)
     elif current_sum > upper_bound:
         print(colored("Warnung: Die erreichte Summe liegt oberhalb der oberen Grenze:", "red"), current_sum, upper_bound)
     else:
         print(colored("Die Summe liegt innerhalb der Grenzen:", "green"), current_sum, lower_bound, upper_bound)
     print("Ausgewählte Takte:", sorted_selection, "Gesamt:", len(measure_selection), "Ausgewählte Elemente:", 
           selected_elements, "Gesamt:", sum(selected_elements), "Versuche:", attempts, "Maximale Versuche:", max_attempts)
     return sorted_selection, state

