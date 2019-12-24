"""Get/set EXIF dates from photos"""

import exifread
from icloudpd.logger import setup_logger
import datetime


def get_photo_exif(path):
    """Get EXIF date for a photo, returning None on error"""
    try:
        with open(path, 'rb') as file:
            exif_dict = exifread.process_file(file, details=False, stop_tag='DateTimeOriginal')
            exif_date_tag = exif_dict.get('EXIF DateTimeOriginal')
            if exif_date_tag:
                return str(exif_date_tag)
            else:
                return None
    except Exception as e:
        logger = setup_logger()
        logger.debug("%s fetching EXIF data for %s", e.__class__.__name__, path)
        return None


def exif_to_unix_local(exif_date):
    # strptime returns in local timezone
    return datetime.datetime.strptime(exif_date, "%Y:%m:%d %H:%M:%S").timestamp()
