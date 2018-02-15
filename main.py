import sys

import parse
import session_manager
import storage_manager


def main():
    """
    Main script.

    Parse arguments and take the action specified by the user.
    """
    parser = parse.prepare_parser()
    args = parser.parse_args()

    storage_manager.prepare_storage_dir()

    if args.list:
        session_manager.list_sessions()
    elif args.save:
        session_manager.save_session(args.save)
    elif args.restore:
        session_manager.restore_session(args.restore)
    elif args.delete:
        session_manager.delete_session(args.delete)
    elif args.backup:
        session_manager.backup_saved_sessions()
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
