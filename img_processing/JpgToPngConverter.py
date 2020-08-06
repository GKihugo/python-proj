import os
import sys
from PIL import Image


#Grabbing the path in cmd
images_folder=sys.argv[1]
new_images=sys.argv[2]

#creating and checking new path for new image
if not os.path.exists(new_images):
	os.makedirs(new_images)

for filename in os.listdir(images_folder):
	new_img=Image.open(f'{images_folder}{filename}')
	clean_name=os.path.splitext(filename)[0] #to get rid of 'jpg name'
	new_img.save(f'{new_images}{clean_name}.png','png')
	print('has been succesfully converted')