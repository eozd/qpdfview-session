import os

import constants


def prepare_storage_dir():
    """
    Create the storage directory if it doesn't exist.
    """
    if not os.path.exists(constants.storage_dir):
        os.makedirs(constants.storage_dir)
