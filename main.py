import numpy as np
import scrape
import matplotlib.pyplot as plt

# adding tuning would be kinda cool too
notes = np.array(['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] * 3)
scales = {'Acoustic': [0, 2, 4, 6, 7, 9, 10], 'Aeolian mode or natural minor': [0, 2, 3, 5, 7, 8, 10], 'Algerian': [0, 2, 3, 6, 7, 8, 11, 12, 14, 15], 'Altered or Super Locrian': [0, 1, 3, 4, 6, 8, 10], 'Augmented': [0, 3, 4, 7, 8, 11], 'Bebop dominant': [0, 2, 4, 5, 7, 9, 10, 11], 'Blues': [0, 3, 5, 6, 7, 10], 'Chromatic': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'Dorian mode': [0, 2, 3, 5, 7, 9, 10], 'Double harmonic': [0, 1, 4, 5, 7, 8, 11], 'Enigmatic': [0, 1, 4, 6, 8, 10, 11], 'Flamenco mode': [0, 1, 4, 5, 7, 8, 11], '"Gypsy"': [0, 2, 3, 6, 7, 8, 10], 'Half diminished': [0, 2, 3, 5, 6, 8, 10], 'Harmonic major': [0, 2, 4, 5, 7, 8, 11], 'Harmonic minor': [0, 2, 3, 5, 7, 8, 11], 'Hirajoshi': [0, 4, 6, 7, 11], 'Hungarian "Gypsy"/Hungarian minor': [0, 2, 3, 6, 7, 8, 11], 'Hungarian major': [0, 3, 4, 6, 7, 9, 10], 'In': [0, 1, 5, 7, 8], 'Insen': [0, 1, 5, 7, 11], 'Ionian mode or major': [0, 2, 4, 5, 7, 9, 11], 'Istrian': [0, 1, 3, 4, 6], 'Iwato': [0, 1, 5, 6, 10], 'Locrian mode': [0, 1, 3, 5, 6, 8, 10], 'Lydian augmented': [0, 2, 4, 6, 8, 9, 11], 'Lydian mode': [0, 2, 4, 6, 7, 9, 11], 'Major bebop': [0, 2, 4, 5, 7, 8, 9, 11], 'Major Locrian': [0, 2, 4, 5, 6, 8, 10], 'Major pentatonic': [0, 2, 4, 7, 9], 'Melodic minor (ascending)': [0, 2, 3, 5, 7, 9, 11], 'Minor pentatonic': [0, 3, 5, 7, 10], 'Mixolydian mode or Adonai malakh mode': [0, 2, 4, 5, 7, 9, 10], 'Neapolitan major': [0, 1, 3, 5, 7, 9, 11], 'Neapolitan minor': [0, 1, 3, 5, 7, 8, 11], 'Persian': [0, 1, 4, 5, 6, 8, 11], 'Phrygian dominant': [0, 1, 4, 5, 7, 8, 10], 'Phrygian mode': [0, 1, 3, 5, 7, 8, 10], 'Prometheus': [0, 2, 4, 6, 9, 10], 'Scale of harmonics': [0, 3, 4, 5, 7, 9], 'Tritone': [0, 1, 4, 6, 7, 10], 'Two-semitone tritone': [0, 1, 2, 6, 7], 'Ukrainian Dorian': [0, 2, 3, 6, 7, 9, 10], 'Whole tone': [0, 2, 4, 6, 8, 10], 'Yo': [0, 3, 5, 7, 10], 'Melodic minor (descending)': [0, 2, 4, 5, 7, 9, 10], 'Octatonic (Mode 1)': [0, 2, 3, 5, 6, 8, 9, 11], 'Octatonic (Mode 2)': [0, 1, 3, 4, 6, 7, 9]}


def get_notes(root, scale):
    root_index = notes.tolist().index(root)
    octave = notes[root_index:root_index + 12]
    indices = scales[scale]
    return np.take(octave, indices)


if __name__ == '__main__':
    # scales = scrape.get_scales()
    # print(scales)
    print(get_notes('C', 'Acoustic'))