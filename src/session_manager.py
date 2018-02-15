import shutil
import os
import sys
import argparse

import qpdfview_session.constants as constants


def list_sessions():
    """
    List all the previously saved sessions.
    """
    for session_name in os.listdir(constants.session_dir):
        print(session_name)


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
    print('Current session is saved to {}'.format(save_path))


def restore_session(session_name):
    """
    Restore a previously saved session with the given session name.

    Before restoring the session, take a backup of the current qpdfview session.

    Parameters
    ----------
    session_name : str
        Name of the session to restore.
    """
    restore_path = os.path.join(constants.session_dir, session_name)

    if os.path.exists(restore_path):
        shutil.copy(constants.qpdfview_database_path, constants.backup_path)
        print('Current session is saved to {}'.format(constants.backup_path))
        shutil.copy(restore_path, constants.qpdfview_database_path)
        print('{} session is restored'.format(session_name))
    else:
        print('No such session: {}'.format(session_name))


def delete_session(session_name):
    """
    Delete a previously saved session with the given session name.

    Parameters
    ----------
    session_name : str
        Name of the session to delete.
    """
    delete_path = os.path.join(constants.session_dir, session_name)

    if os.path.exists(delete_path):
        os.remove(delete_path)
        print('{} session is deleted'.format(session_name))
    else:
        print('No such session: {}'.format(session_name))


def backup_saved_sessions():
    """
    Backup all the previously saved sessions to the backup directory.
    """
    if os.path.exists(constants.backup_dir):
        shutil.rmtree(constants.backup_dir)
        print('Previous backups are deleted')

    shutil.copytree(constants.session_dir, constants.backup_dir)
    print('All saved sessions are copied to {}'.format(constants.backup_dir))
