import os, shutil
import pandas as pd

def compile_images():
    # read all images from the grocery_images_png directory and output
    images_src_path = '../grocery_images_png/'
    images_dest_path = '../all_images/'
    dirs = os.listdir(images_src_path)

    for dir in dirs:
        filenames = os.listdir(os.path.join(images_src_path, dir))
        for fn in filenames:
            src = os.path.join(images_src_path, dir, fn)
            shutil.copy(src, images_dest_path)

def change_file_names():
    # read the csv file with old names -> convert to .png
    label_path = '../train.csv'
    df = pd.read_csv(label_path)

    def change_extensions(row):
        if row.file.endswith('.jpeg'):
            row.file = row.file[:-5] + '.png'
        return row.file

    df.file = df.apply(change_extensions, axis=1)
    df.to_csv('image_labels.csv')

compile_images()
