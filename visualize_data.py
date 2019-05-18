import os
from os import listdir
from os.path import isfile, join
import shutil
import stat
import collections
from collections import defaultdict

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

grocery_images_dir = '../grocery_images_png/'
img_rows = 5
img_cols = 5

fig, ax = plt.subplots(img_rows, img_cols, figsize=(25, 50))
plt.subtitle('Random Grocery Images', fontsize=20)

sorted_img_dirs = sorted(os.listdir(grocery_images_dir))
for row in range(img_rows):
    for col in range(img_cols):
        try:
            # get an individual food category to draw
            spec_img_dir = sorted_img_dirs[col + row*5]
        except:
            break
        # get all the images in the specified directory
        all_images = os.listdir(os.path.join(grocery_images_dir, spec_img_dir))
        # open a random one and show
        img_path = np.random.choice(all_images)
        img = plt.imread(os.path.join(grocery_images_dir, spec_img_dir, img_path))
        ax[row][col].imshow(img)
        ec = (0, .6, .1)
        fc = (0, .7, .2)
        ax[row][col].text(0, -20, spec_img_dir, size=10, rotation=0,
        ha="left", va="top",
        bbox=dict(boxstyle="round", ec=ec, fc=fc))

plt.show()
