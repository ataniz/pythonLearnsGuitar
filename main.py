import numpy as np
# import scrape
import matplotlib.pyplot as plt

# adding tuning would be kinda cool too

notes = np.array(['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] * 3)
scales = {'Acoustic scale': [0, 2, 4, 6, 7, 9, 10, 12],
          'Aeolian mode or natural minor scale': [0, 2, 3, 5, 7, 8, 10, 12],
          'Algerian scale': [0, 2, 3, 6, 7, 8, 11, 12, 14, 15, 17],
          'Altered scale or Super Locrian scale': [0, 1, 3, 4, 6, 8, 10, 12],
          'Augmented scale': [0, 3, 4, 7, 8, 11, 12], 'Bebop dominant scale': [0, 2, 4, 5, 7, 9, 10, 11, 12],
          'Blues scale': [0, 3, 5, 6, 7, 10, 12], 'Chromatic scale': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
          'Dorian mode': [0, 2, 3, 5, 7, 9, 10, 12], 'Double harmonic scale': [0, 1, 4, 5, 7, 8, 11, 12],
          'Enigmatic scale': [0, 1, 4, 6, 8, 10, 11, 12], 'Flamenco mode': [0, 1, 4, 5, 7, 8, 11, 12],
          '"Gypsy" scale': [0, 2, 3, 6, 7, 8, 10, 12], 'Half diminished scale': [0, 2, 3, 5, 6, 8, 10, 12],
          'Harmonic major scale': [0, 2, 4, 5, 7, 8, 11, 12], 'Harmonic minor scale': [0, 2, 3, 5, 7, 8, 11, 12],
          'Hirajoshi scale': [0, 4, 6, 7, 11, 12],
          'Hungarian "Gypsy" scale/Hungarian minor scale': [0, 2, 3, 6, 7, 8, 11, 12],
          'Hungarian major scale': [0, 3, 4, 6, 7, 9, 10, 12], 'In scale': [0, 1, 5, 7, 8, 12],
          'Insen scale': [0, 1, 5, 7, 11, 13], 'Ionian mode or major scale': [0, 2, 4, 5, 7, 9, 11, 12],
          'Istrian scale': [0, 1, 3, 4, 6, 7], 'Iwato scale': [0, 1, 5, 6, 10, 12],
          'Locrian mode': [0, 1, 3, 5, 6, 8, 10, 12], 'Lydian augmented scale': [0, 2, 4, 6, 8, 9, 11, 12],
          'Lydian mode': [0, 2, 4, 6, 7, 9, 11, 12], 'Major bebop scale': [0, 2, 4, 5, 7, 8, 9, 11, 12],
          'Major Locrian scale': [0, 2, 4, 5, 6, 8, 10, 12], 'Major pentatonic scale': [0, 2, 4, 7, 9, 12],
          'Melodic minor scale (ascending)': [0, 2, 3, 5, 7, 9, 11, 12], 'Minor pentatonic scale': [0, 3, 5, 7, 10, 12],
          'Mixolydian mode or Adonai malakh mode': [0, 2, 4, 5, 7, 9, 10, 12],
          'Neapolitan major scale': [0, 1, 3, 5, 7, 9, 11, 12], 'Neapolitan minor scale': [0, 1, 3, 5, 7, 8, 11, 12],
          'Persian scale': [0, 1, 4, 5, 6, 8, 11, 12], 'Phrygian dominant scale': [0, 1, 4, 5, 7, 8, 10, 12],
          'Phrygian mode': [0, 1, 3, 5, 7, 8, 10, 12], 'Prometheus scale': [0, 2, 4, 6, 9, 10, 12],
          'Scale of harmonics': [0, 3, 4, 5, 7, 9, 12], 'Tritone scale': [0, 1, 4, 6, 7, 10, 12],
          'Two-semitone tritone scale': [0, 1, 2, 6, 7, 8], 'Ukrainian Dorian scale': [0, 2, 3, 6, 7, 9, 10, 12],
          'Whole tone scale': [0, 2, 4, 6, 8, 10, 12], 'Yo scale': [0, 3, 5, 7, 10, 12],
          'Melodic minor scale (descending)': [0, 2, 4, 5, 7, 9, 10, 12],
          'Octatonic scale (Mode 1)': [0, 2, 3, 5, 6, 8, 9, 11, 12],
          'Octatonic scale (Mode 2)': [0, 1, 3, 4, 6, 7, 9, 10]}


def get_notes(indices):
    # to make things easier lets start from 1 while calling this function
    indices = np.array(indices) - 1
    return np.take(notes, indices)


def get_scale(root, scale):
    if __name__ == '__main__':
        # scales = scrape.get_scales()
        print(scales)
