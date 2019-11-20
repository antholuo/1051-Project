"""This is the Improved Edge Detection Test from group L2-5."""

from Cimpl import *
from L2_5_P5_detect_edges_better import betterEdgeDetect


def edgeTest() -> str:
    """
    Test function that checks if the r, g, b components have been correctly altered by the Improved Edge Detection filter. According to the threshold value inputed by the user and whether the contrast between two pixels is low or high, the pixel will be changed to either white or black. If this is successfully executed and the pixels in the image are correctly altered, the test function returns "PASS" to the user. If this is not the case, test function returns "FAIL".
    
    Written by Alia Nichol (#101143486). 
    >>> edgeTest(image)
    """

    fails = 0  # creating a counter for the number of pixels that fail to change to the correct colour
    # putting the original image through the Improved Edge Detection Filter
    new_img = betterEdgeDetect(image, threshold)

    for y in range(get_height(image) - 1):
        for x in range(get_width(image) - 1):

            r, g, b = tuple(get_color(image, x, y))
            # accounting for the pixels below
            r1, g1, b1 = tuple(get_color(image, x, y + 1))
            # accounting for the pixels to the right
            r2, g2, b2 = tuple(get_color(image, x + 1, y))

            if abs(((r + g + b) // 3) - ((r1 + g1 + b1) // 3)) > threshold or abs(((r + g + b) // 3) - ((r2 + g2 + b2) // 3)) > threshold:
                if r2 != 0 and g2 != 0 and b2 != 0:
                    fails += 1

            # NOTE: NOT SURE IF I NEED TO DO >=
            elif abs(((r + g + b) // 3) - ((r1 + g1 + b1) // 3)) <= threshold or abs(((r + g + b) // 3) - ((r2 + g2 + b2) // 3)) <= threshold:
                if r2 != 255 and g2 != 255 and b2 != 255:
                    fails += 1

    if fails == 0:
        print("PASS")
    else:
        print("FAIL")


if __name__ == '__main__':
    edgeTest()
