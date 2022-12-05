import os
import shutil

# The path to the folder containing duplicate images
folder_path = 'C:/Users/YourUserName/Pictures/DuplicateImages/'

# Create a dictionary to store the images and their paths
# The key will be the image file name
# The value will be the complete path to the image
images_dict = {}

# Loop through the folder and get the images
for filename in os.listdir(folder_path):
    # The complete path to the image
    image_path = os.path.join(folder_path, filename)
    # Add the image and its path to the dictionary
    images_dict[filename] = image_path

# Loop through the images in the dictionary
for image_name, image_path in images_dict.items():
    # The path of the folder containing the duplicate images
    duplicate_folder_path = os.path.join(folder_path, 'duplicates')
    # Check if the folder exists
    if not os.path.isdir(duplicate_folder_path):
        # Create the folder if it doesn't exist
        os.mkdir(duplicate_folder_path)
    # The path of the duplicate image
    duplicate_image_path = os.path.join(duplicate_folder_path, image_name)
    # Check if the image already exists in the duplicate folder
    if os.path.isfile(duplicate_image_path):
        # Delete the duplicate image if it exists
        os.remove(image_path)
    else:
        # Move the image to the duplicate folder if it doesn't exist
        shutil.move(image_path, duplicate_folder_path)
