#!/usr/bin/env python3
# coding: utf-8
"""
main.py
10-16-2020
jack skrable
"""

import numpy as np
from PIL import Image

# read image
im = Image.open('./images/branch.jpg')

# convert to array
im_arr = np.array(im)

# convert to image
im_new = Image.fromarray(im_arr)


def show_image(arr):
    print('Displaying image...')
    Image.fromarray(arr).show()


def color_boost(arr, color='green', scale=2):
    """
    Takes in a 3D array of RGB pixels.
    Boosts color in param by multiplying pixel value by scale.
    Reduces other colors by dividing by scale.
    Returns 3D array of RGB pixels.
    """
    # tuples breaking logic somehow?
    # color_map = {'red': 0, 'green': 1, 'blue':2, 'yellow':(0,1), 'purple': (0,2), 'turquoise': (1,2)}
    color_map = {'red': 0, 'green': 1, 'blue':2}
    print('Boosting {}...'.format(color))
    edit = np.copy(arr)
    if type(color_map[color]) is tuple:
        for col in color_map[color]:
            edit[:,:,color_map[col]] = arr[:,:,color_map[col]] * scale    
    else:
        edit[:,:,color_map[color]] = arr[:,:,color_map[color]] * scale
    edit[:,:,color_map[color]] = arr[:,:,color_map[color]] * scale
    for color in [k for k in color_map if k not in color]:
        edit[:,:,color_map[color]] = arr[:,:,color_map[color]] / scale

    return edit



def color_extract(arr, color):
    """
    Takes in a 3D array of RGB pixels.
    Extracts pixel values only of the specified color.
    Returns 3D array of RGB pixels.
    """
    color_map = {'red': 0, 'green': 1, 'blue':2}

    edit = np.copy(arr)
    edit[:,:,color_map[color]] = arr[:,:,color_map[color]]
    for color in [k for k in color_map if k not in color]:
        edit[:,:,color_map[color]] = 0

    return edit


def gamma_compression(arr):
    """
    Takes in a 3D array of RGB pixels.
    Using linear approximation of gamma compression, converts
    to grayscale. Sums the linear equation, makes RGB equal to the sum.
    Returns 3D array of RGB pixels.
    """
    print('Converting to grayscale...')
    edit = np.copy(arr)
    edit[:,:,0] = arr[:,:,0] * 0.299
    edit[:,:,1] = arr[:,:,1] * 0.587
    edit[:,:,2] = arr[:,:,2] * 0.114
    gray = np.expand_dims(edit.sum(axis=2), axis=2)
    final = np.uint8(np.append(gray, np.append(gray, gray, 2), 2))
    return final
