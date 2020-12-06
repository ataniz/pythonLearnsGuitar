import numpy as np
import matplotlib.pyplot as plt

# adding tuning would be kinda cool too

notes = np.array(['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] * 3)

scales = {

}


def get_notes(indices):
    # to make things easier lets start from 1 while calling this function
    indices = np.array(indices) - 1
    return np.take(notes, indices)

# def get_scales(scale, root):
