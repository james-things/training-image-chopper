# import image class from PIL module
from PIL import Image
import os

# capture, save, and label image at the given position
def capture_and_save_image(img, x1, y1, x2, y2, image_name, position):
	cur_im = img.crop((x1, y1, x2, y2))
	cur_im.save(f"out/{image_name}-{position}.png")

def log_debug(output_size, travel_range, is_landscape, x1, y1, x2, y2):
	print(f'position: start, output_size {output_size} travel_range {travel_range} is_landscape {is_landscape}')
	print(f'x1 {x1} y1 {y1} x2 {x2} y2 {y2}')

# process an individual image, producing three output images	
def process_image(image_name, image_file_path):
	im = Image.open(rf"{full_path}")
	 
	# size of the image in pixels
	width, height = im.size

	# determine image orientation
	is_landscape = (width > height)

	# output size is lesser of width or height
	output_size = min(width, height)
	travel_range = max(width, height)

	# define initial square (top left)
	x1 = 0
	x2 = output_size
	y1 = 0
	y2 = output_size

	# capture initial square
	capture_and_save_image(im, x1, y1, x2, y2, image_name, "start")
	log_debug(output_size, travel_range, is_landscape, x1, y1, x2, y2)

	# shift to middle
	middle_point = travel_range / 2
	middle_image_start = middle_point - (output_size / 2)
	middle_image_end = middle_point + ((output_size / 2) - 1)

	if is_landscape: 
		x1 = middle_image_start
		x2 = middle_image_end
	else:
		y1 = middle_image_start
		y2 = middle_image_end
		
	# capture middle square
	capture_and_save_image(im, x1, y1, x2, y2, image_name, "middle")
	log_debug(output_size, travel_range, is_landscape, x1, y1, x2, y2)

	# shift to end
	end_point = travel_range
	end_image_start = travel_range - output_size

	if is_landscape: 
		x1 = end_image_start
		x2 = travel_range
	else:
		y1 = end_image_start
		y2 = travel_range

	# capture final square
	capture_and_save_image(im, x1, y1, x2, y2, image_name, "end")
	log_debug(output_size, travel_range, is_landscape, x1, y1, x2, y2)

	print("~image completed~")

## SCRIPT START ## 
target_path = os.path.dirname(os.path.realpath(__file__)) + "\\"
if not os.path.isdir('./out'):
	os.mkdir('./out')

for imagefile in os.listdir("./"):
    full_path = target_path + imagefile
    filename_split = imagefile.split('.')
    filename = filename_split[0]
    if not os.path.isdir(full_path):
    	if filename_split[len(filename_split)-1] == "png" or filename_split[len(filename_split)-1] == "jpg":
    		print(f'processing: {filename}')
    		process_image(filename, full_path)
