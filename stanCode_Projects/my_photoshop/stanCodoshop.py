"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    color_distance = math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    # total RGB
    red_t = 0
    green_t = 0
    blue_t = 0

    # Plus all pixels' RGB
    for i in range(len(pixels)):
        red_t += pixels[i].red
        green_t += pixels[i].green
        blue_t += pixels[i].blue

    # Get the average of RGB
    red_avg = red_t // len(pixels)
    green_avg = green_t // len(pixels)
    blue_avg = blue_t // len(pixels)
    average = [red_avg, green_avg, blue_avg]
    return average


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    average_rgb = get_average(pixels)
    avg_red = average_rgb[0]
    avg_green = average_rgb[1]
    avg_blue = average_rgb[2]

    minimum = get_pixel_dist(pixels[0], avg_red, avg_green, avg_blue)
    min_pix = []
    if len(pixels) == 1:
        min_pix = pixels[0]
        return min_pix
    else:
        for i in range(1, len(pixels)):
            dist = get_pixel_dist(pixels[i], avg_red, avg_green, avg_blue)
            if dist < minimum:
                minimum = dist
                min_pix = pixels[i]
        if minimum == get_pixel_dist(pixels[0], avg_red, avg_green, avg_blue):
            return pixels[0]
        else:
            return min_pix


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    for x in range(width):
        for y in range(height):
            img_pixel = []
            for i in range(len(images)):
                img_pixel += [images[i].get_pixel(x, y)]
            best_pixel = get_best_pixel(img_pixel)

            # 空白pixel上色
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
