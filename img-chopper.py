# import image class from PIL module
from PIL import Image
import os

# produce and output image at the given position
def capture_and_save_image(x1, y1, x2, y2, img, output_size, image_name):
	cur_im = img.crop((x1, y1, x2, y2))
	if not os.path.isdir(f'./out'):
		print(f'Error: Please create output directory: ./out')
	else:
		cur_im.save(f"out/{image_name}w{x1}h{y1}.png")

# process an individual image, producing three output images	
def process_image(image_name, image_file_path):
	im = Image.open(rf"{full_path}")
	 
	# size of the image in pixels
	width, height = im.size

	# determine image orientation
	is_landscape = (width > height)

	# output size is lesser of width or height
	output_size = min(width, height)

	# set initial square (top left)
	x1 = 0
	x2 = output_size
	y1 = 0
	y2 = output_size

	# set movement increment
	increment = (output_size / 3) / 2

	# capture initial square
	capture_and_save_image(x1, y1, x2, y2, im, output_size, image_name)

	# perform first shift
	if is_landscape: 
		x1 += increment
		x2 += increment
	else:
		y1 += increment
		y2 += increment
		
	# capture middle square
	capture_and_save_image(x1, y1, x2, y2, im, output_size, image_name)

	# perform second shift
	if is_landscape: 
		x1 += increment
		x2 += increment
	else:
		y1 += increment
		y2 += increment

	# capture final square
	capture_and_save_image(x1, y1, x2, y2, im, output_size, image_name)
	
	print("~image completed~")

## SCRIPT START ## 
target_path = os.path.dirname(os.path.realpath(__file__)) + "\\"

for imagefile in os.listdir("./"):
    full_path = target_path + imagefile
    filename_split = imagefile.split('.')
    filename = filename_split[0]
    if not os.path.isdir(full_path):
    	if filename_split[len(filename_split)-1] == "png" or filename_split[len(filename_split)-1] == "jpg":
    		print(f'processing: {filename}')
    		process_image(filename, full_path)
