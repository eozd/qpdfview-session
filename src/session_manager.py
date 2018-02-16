import shutil
import os
import sys
import argparse

import qpdfview_session.constants as constants


def list_sessions():
    """
    Return a list all the previously saved session names.

    Returns
    -------
    session_list : list
        List of previously saved session names.
    """
    return os.listdir(constants.session_dir)


def save_session(session_name):
    """
    Save the current qpdfview session to a session with the given name.

    Parameters
    ----------
    session_name : str
        Name of the saved session.
    """
    save_path = os.path.join(constants.session_dir, session_name)
    shutil.copy(constants.qpdfview_database_path, save_path)


def restore_session(session_name):
    """
    Restore a previously saved session with the given session name.

    Before restoring the session, take a backup of the current qpdfview session.

    Parameters
    ----------
    session_name : str
        Name of the session to restore.

    Raises
    ------
    ValueError
        If the session with the given name doesn't exist.
    """
    restore_path = os.path.join(constants.session_dir, session_name)

    try:
        shutil.copy(restore_path, constants.qpdfview_database_path)
    except FileNotFoundError:
        raise ValueError('No such session: {}'.format(session_name))


def delete_session(session_name):
    """
    Delete a previously saved session with the given session name.

    Parameters
    ----------
    session_name : str
        Name of the session to delete.

    Raises
    ------
    ValueError
        If the session with the given name doesn't exist
    """
    delete_path = os.path.join(constants.session_dir, session_name)

    try:
        os.remove(delete_path)
    except FileNotFoundError:
        raise ValueError('No such session: {}'.format(session_name))


def backup_saved_sessions():
    """
    Backup all the previously saved sessions to the backup directory.
    """
    if os.path.exists(constants.backup_dir):
        shutil.rmtree(constants.backup_dir)

    shutil.copytree(constants.session_dir, constants.backup_dir)


def clean_session():
    """
    Clean the current session and get rid of all tabs and bookmarks.

    Raises
    ------
    ValueError
        If there is no session to clean
    """
    try:
        os.remove(constants.qpdfview_database_path)
    except FileNotFoundError:
        raise ValueError('There was no session to clean')
