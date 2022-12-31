# training-image-chopper

 A handy python script to cut rectangular images into the largest possible beginning, middle, and end squares, regardless of their orientation, for use in training datasets!

 To use, you will need to install install https://pillow.readthedocs.io/en/stable/ (or use an existing python/anaconda environment with PIL configured).

 As the script is currently written, you must create a folder titled "out" in the same directory as your images for the output images to be saved to.

 To use the script, naviate to your target directory and execute the script. For example, if the script is in the same directory as the target images:

 
  `cd x:/target-path/`
  
  `mkdir out`
  
  `python img-chopper.py`
 
 
