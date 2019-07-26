#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse


def insert_import_path(string_path):
    sys.path.insert(0, string_path)


def insert_package_path():
    current_file_path = os.path.abspath(__file__)
    current_file_dir = os.path.dirname(current_file_path)
    parent_file_dir = os.path.join(current_file_dir, '../')
    insert_import_path(current_file_dir)
    insert_import_path(parent_file_dir)
    return


try:
    # 自定义import路径
    insert_package_path()
    from secure_delete import secure_delete
except ImportError:
    import secure_delete
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('PATH', nargs='?', type=str)
    parser.add_argument('--count', default=1, type=int)
    parser.add_argument('--wipe_free_space', action='store_true')
    parser.add_argument('--upset_inodes', action='store_true')
    args = parser.parse_args()
    if args.PATH is None:
        parser.print_help()
        exit(0)
    if os.path.exists(args.PATH) is False:
        pass
    else:
        secure_delete.secure_delete(args.PATH, args.count)
    if args.wipe_free_space is True:
        secure_delete.wipe_free_space(args.PATH)
    if args.upset_inodes is True:
        secure_delete.upset_inodes(args.PATH, args.count)
    return


if __name__ == '__main__':
    main()
    pass
