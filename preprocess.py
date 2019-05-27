
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import pandas as pd
import random
from scipy.misc import imresize
'''
# import multiprocessing tool for data augmentation
import multiprocessing as mp

num_processes = 6
pool = mp.Pool(processes=num_processes)
'''
TRAIN_PATH = '../Datasets/Train/'
TEST_PATH = '../Datasets/Test/'

# global class_indices for label encoding
class_to_ind = {}
ind_to_class = {}

# Load dataset images and resize to meet minimum width and height pixel size
def load_images(root, min_side=299):
    #while True:
    frac = 0.05
    all_imgs = []
    all_classes = []
    resize_count = 0
    invalid_count = 0
    for i, subdir in enumerate(os.listdir(root)):
        imgs = os.listdir(os.path.join(root, subdir))
        # load only the required number of images
        num_imgs = len(imgs)
        req_num_imgs = int(frac*num_imgs)
        random.shuffle(imgs)
        imgs = imgs[:req_num_imgs]

        class_ind = class_to_ind[subdir]
        print(i, class_ind, subdir)
        for img_name in imgs:
            img_arr = img.imread(os.path.join(root, subdir, img_name))
            img_arr_rs = img_arr
            try:
                w, h, _ = img_arr.shape
                if w < min_side:
                    wpercent = (min_side/float(w))
                    hsize = int((float(h)*float(wpercent)))
                    #print('new dims:', min_side, hsize)
                    img_arr_rs = imresize(img_arr, (min_side, hsize))
                    resize_count += 1
                elif h < min_side:
                    hpercent = (min_side/float(h))
                    wsize = int((float(w)*float(hpercent)))
                    #print('new dims:', wsize, min_side)
                    img_arr_rs = imresize(img_arr, (wsize, min_side))
                    resize_count += 1
                all_imgs.append(img_arr_rs)
                all_classes.append(class_ind)
            except:
                print('Skipping bad image: ', subdir, img_name)
                invalid_count += 1
    print(len(all_imgs), 'images loaded')
    print(resize_count, 'images resized')
    print(invalid_count, 'images skipped')
    #X_train, y_train = np.array(all_imgs), np.array(all_classes)
    #yield tuple(zip(X_train, y_train))
    return np.array(all_imgs).reshape(-1), np.array(all_classes)

def image_generator():
    #while True:
    # load the test sets when needed, and clear the X_train variables
    #X_test, y_test = load_images(TEST_PATH, frac=0.3, min_side=299)
    X_train, y_train = load_images(TRAIN_PATH, frac=0.05, min_side=299)
    '''
    # shuffle
    temp_df = pd.DataFrame({'x': X_train, 'y': y_train})
    temp_df = temp_df.sample(frac=1)
    X_train = temp_df.x.to_numpy()
    y_train = temp_df.y.to_numpy()
    '''
    yield tuple(zip(X_train, y_train))

classes = os.listdir(TRAIN_PATH)
ind_to_class = dict(zip(range(len(classes)), classes))
class_to_ind = {c:i for i, c in ind_to_class.items()}
print(class_to_ind)
