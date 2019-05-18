import os, shutil
import pandas as pd

images_src_path = '../train/'
images_dest_path = '../grocery_images/'

dir_df = pd.read_csv('../train.csv')

print(dir_df.head())

# for each row in the df, find the "file" in the images_src_path, copy the file into the directory specified by "label" of the row
# create new dir only if not exists

filenames = os.listdir(images_src_path)

print(os.path.exists(images_dest_path))

for fn in filenames:
    spec_dir_name = dir_df[dir_df.file == fn].iloc[0].label
    output_dir = images_dest_path + spec_dir_name

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    shutil.copy(images_src_path + fn, output_dir)
