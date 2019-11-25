from L2_5_image_filters import create_red, create_blue, green_filter, combine, extreme_contrast, posterize, sepia, \
    two_tone, three_tone, detect_edges, detect_edges_better, flip_horizontal, flip_vertical
from typing import Tuple
from Cimpl import load_image, create_color, set_color, show, Image, save_as, get_width, get_height, copy, \
    create_image, save_as, get_color, choose_file, copy
import os

def prompt(command: str) ->str :
    """
    Prompts the user for an input. Checks validity before returning an
    """
    command = input("Please enter a command from the following list: [L, S, 2, 3, X, T, P, E, I, V, H, Q]")
    
    all_commands = ["L", "S", "2", "3", "X", "T", "P", "E", "I", "V", "H", "Q"]
   
    while command in all_commands:
        pass
    
    print("Prompt is not valid. Please Try Again")

def is_valid():
    """
    checks the validity of the input
    :return:
    :rtype:
    """

def apply_filter(selection, image: Image, additional1 = None, additional2 = None, additional3 = None) -> Image:
    """
    Applies the selected filter.
    """

    functions = [two_tone, three_tone, extreme_contrast, sepia, posterize, detect_edges, detect_edges_better, flip_vertical, flip_horizontal]
    prompts = ['2', '3', 'X', 'T', 'P', 'E', 'I', 'V', 'H']
    for index in range(len(prompts)):
        if selection == prompts[index]:
            fn = functions[index]
            return fn(image)


def main():
    image = load_image(choose_file())
    while True:
        image = apply_filter(prompt(), image)

if __name__ == '__main__':
    new_path = os.getcwd() + '/returns'  # creates path
    try:
        os.mkdir(new_path)
    except:
        pass
    main()