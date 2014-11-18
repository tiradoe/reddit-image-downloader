#!/usr/bin/env python
"""
Random background changer for Gnome 3
Author: Edward Tirado Jr
License: MIT
"""

from os import walk, path
import sys
import random
import subprocess
import time


def getImages(image_path):
    for(dirpath, dirnames, filenames) in walk(image_path):
        images.extend(filenames)
        break


def setRandomImage(image_path, images):
    image_position = random.randrange(0, len(images))
    current_image = images[image_position]

    subprocess.call(
        'gsettings set org.gnome.desktop.background picture-uri file:///' +
        path.abspath(image_path) + '/' + current_image, shell=True)

    time.sleep(int(frequency))


images = []
script, image_path, frequency = sys.argv

getImages(image_path)

while(True):
    setRandomImage(image_path, images)
