from .constants import INITIAL_IMAGES_PATH
import os
from pathlib import Path
from django.conf import settings
from uuid import uuid4


def get_image_format(path):
    """
    Get the image format from the path
    """
    return path.split('.')[-1]


def fix_spaces(text):
    """
    Replace all spaces with underscores
    """
    return text.replace(' ', '_')


def get_image_path(instance, filename):
    while True:
        fixed_title = str(uuid4())
        path = f'{INITIAL_IMAGES_PATH}{fixed_title}.{get_image_format(filename)}'
        image_path = f'{settings.MEDIA_ROOT}/{path}'
        if not Path(image_path).is_file():
            break
    return path
