import pandas as pd
import os, shutil

# train/test split
'''
1. Script to copy all images from the png folder into one folder for all images of all classes.
2. Read the csv file of names, convert all the names also to png, save into another csv, img_png_labels.csv
3. Randomly select 30% of the elements from the new img_png_labels df and put them in Test folder, and the rest in Train
'''

df = pd.read_csv('image_labels.csv')

test_df = df.sample(frac=0.3, random_state=0)
train_df = df.drop(test_df.index, axis=0)
df.drop(['Unnamed: 0'], axis=1)

images_src_path = '../all_png_images/all_images/'
train_path = '../all_png_images/Train/'
test_path = '../all_png_images/Test/'

if os.path.exists(train_path) or os.path.exists(test_path):
    raise Exception('Error: Train/Test split already exists!')

os.makedirs(train_path)
os.makedirs(test_path)

# save the train/test partition for future reference
train_filenames = train_df.loc[:, 'file'].to_numpy().tolist()
test_filenames = test_df.loc[:, 'file'].to_numpy().tolist()

for name in train_filenames:
    shutil.copy(os.path.join(images_src_path, name), os.path.join(train_path, name))

for name in test_filenames:
    shutil.copy(os.path.join(images_src_path, name), os.path.join(test_path, name))

def copy_files(input_path, output_path):

    filenames = os.listdir(input_path)

    for fn in filenames:
        spec_dir_name = df[df.file == fn].iloc[0].label
        output_dir = output_path + spec_dir_name

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        shutil.copy(os.path.join(input_path, fn), output_dir)

# for each file in Train and Test folder, put them in their image category folder
output_train_path = '../Datasets/Train/'
output_test_path = '../Datasets/Test/'
copy_files(train_path, output_train_path)
copy_files(test_path, output_test_path)
