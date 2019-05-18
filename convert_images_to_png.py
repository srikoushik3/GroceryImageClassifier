from PIL import Image, ImageFile
from pathlib import Path
import os, shutil
ImageFile.LOAD_TRUNCATED_IMAGES = True

grocery_images_dir = '../grocery_images/'
grocery_images_dir_png = '../grocery_images_png/'
sorted_img_dirs = sorted(os.listdir(grocery_images_dir))
sorted_img_dirs = sorted_img_dirs[21:]

for spec_img_dir in sorted_img_dirs:
    img_names = os.listdir(os.path.join(grocery_images_dir, spec_img_dir))
    img_save_path = os.path.join(grocery_images_dir_png, spec_img_dir)
    if not os.path.exists(img_save_path):
        os.makedirs(img_save_path)

    for img_name in img_names:
        if img_name.endswith(".jpeg"):
            im = Image.open(os.path.join(grocery_images_dir, spec_img_dir, img_name))
            rgb_im = im.convert('RGB')
            img_mod_path = Path(os.path.join(img_save_path, img_name[:-5] + '.png'))
            rgb_im.save(img_mod_path)
        elif img_name.endswith(".png"):
            shutil.copy(os.path.join(grocery_images_dir, spec_img_dir, img_name), os.path.join(grocery_images_dir_png, spec_img_dir, img_name))
        else:
            print("NOTE: Another file extension! ", img_name)
