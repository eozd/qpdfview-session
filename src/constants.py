import os


storage_dir = os.path.expanduser('~/.qpdfview_session')
session_dir = os.path.join(storage_dir, 'sessions')

backup_dir = os.path.join(storage_dir, 'session_backups')
backup_path = os.path.join(backup_dir, '.restore_session_backup')

qpdfview_database_dir = os.path.expanduser('~/.local/share/qpdfview/qpdfview')
qpdfview_database_path = os.path.join(qpdfview_database_dir, 'database')
