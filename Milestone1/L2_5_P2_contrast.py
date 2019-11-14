from Cimpl import *

image = load_image(choose_file())  # loads the desired image from a given file
show(image)
image1 = copy(image) #creates a copy of the image so it is not overrided when the new image is returned

def extreme_contrast(image):
    """ Given an 
    Written by Alia Nichol
    """    

    for x, y, (r, g, b) in image:  # reads through each pixel in the image
        if 0 < r < 127:
            contrast = create_color(0, g, b)
            set_color(image, x, y, contrast)            
        elif 0 < g < 127:
            contrast = create_color(r, 0, b)
            set_color(image, x, y, contrast)              
        elif 0 < b < 127:
            contrast = create_color(r, g, 0)
            set_color(image, x, y, contrast)              
        elif 128 < r < 255:
            contrast = create_color(255, g, b)
            set_color(image, x, y, contrast)              
        elif 128 < g < 255:
            contrast = create_color(r, 255, b)
            set_color(image, x, y, contrast)             
        elif 128 < b < 255:
            contrast = create_color(r, g, 255)
            set_color(image, x, y, contrast)                 

    save_as(image, 'contrast_channel.png') # saves the image 
    show(load_image('contrast_channel.png'))
    print('contrast_channel saved as new image')
    
    return image1
    