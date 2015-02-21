#!/usr/bin/env python3
"""
Reddit image downloader
Author: Edward Tirado Jr
License: MIT
"""

import sys
import os
import re
import urllib
import praw

EXTENSIONS = set(['.jpg', '.jpeg', '.gif', '.png'])
isPython3 = sys.version_info >= (3, 0)


def isDuplicate(file_name, file_path):
    file_list = os.listdir(file_path)
    file_exists = file_name in file_list
    return file_exists


def isAlbum(link, file_name):
    is_imgur_album = re.match('https?://.*imgur.*\/a\/', link) is not None
    is_imgur_gallery = re.match('https?://.*imgur.*gallery', link) is not None
    has_file_extension = file_name.endswith(tuple(EXTENSIONS))

    if (not is_imgur_album and not is_imgur_gallery) or has_file_extension:
        return False
    else:
        return True


def getContentType(link):
    file_info = urllib.urlopen(link).info()
    return file_info['Content-Type']

if len(sys.argv) < 4:
    print('Not enough arguments: \n' +
          'Need number of images, download directory, and subreddit name')
    sys.exit()


script, image_num, file_path, subreddit = sys.argv

reddit_conn = praw.Reddit(user_agent='Reddit Image Downloader 1.0 by Ed Tirado')
submissions = reddit_conn.get_subreddit(subreddit).get_hot(limit=int(image_num))

for post in submissions:
    link = post.url
    file_name = link.split('/')[-1]
    file_info = getContentType(link)

    if isDuplicate(file_info, file_path) or isAlbum(link, file_name):
        continue

    # Removes any type other than image

    if not file_info.startswith("image"):
        continue

    # Allows images without extensions to download properly.

    if isPython3:
        try:
            urllib.request.urlretrieve(link, file_path + '/' + file_name)
        except Exception:
            continue
    else:
        try:
            # python2 compat
            urllib.urlretrieve(link, file_path + '/' + file_name)
        except:
            continue
