import datetime
import math
import os
import posixpath
import random
import re

from django import template
from django.utils.html import strip_tags

from blog import settings

register = template.Library()


def is_image_file(filename):
    """Does `filename` appear to be an image file?"""
    img_types = [".jpg", ".jpeg", ".png", ".gif", ".svg"]
    ext = os.path.splitext(filename)[1]
    return ext in img_types


@register.simple_tag
def random_image(path):
    """
    Select a random image file from the provided directory
    and return its href. `path` should be relative to MEDIA_ROOT.

    Usage:  <img src='{% random_image "images/whatever/" %}'>
    """
    fullpath = os.path.join(settings.MEDIA_ROOT, path)
    filenames = [f for f in os.listdir(fullpath) if is_image_file(f)]
    pick = random.choice(filenames)
    return posixpath.join(settings.MEDIA_URL, path, pick)


@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)


@register.filter(name='first_word')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)[0]


@register.filter(name='last_word')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)[1]


def count_words(html_string):
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    return count


@register.filter(name='get_read_time')
def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count / 200.0)  # assuming 200 words per minute reading
    # read_time_sec = read_time_min * 60
    read_time = datetime.timedelta(minutes=read_time_min)
    minutes = int(read_time.seconds/60)
    return minutes
