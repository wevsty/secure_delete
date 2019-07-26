#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import secrets
import random


SECURE_BLOCK_SIZE = 1024 * 16


def enum_paths(root_dir, list_paths=list(), **dict_argv):
    bool_include_file = bool(dict_argv.get('include_file', True))
    bool_include_dir = bool(dict_argv.get('include_dir', False))
    bool_recursion_dir = bool(dict_argv.get('recursion_dir', True))
    for sub_path in os.listdir(root_dir):
        full_path = os.path.join(root_dir, sub_path)
        b_is_dir = os.path.isdir(full_path)
        if b_is_dir:
            if bool_recursion_dir is True:
                enum_paths(full_path, list_paths, **dict_argv)
            if bool_include_dir is False:
                pass
            else:
                list_paths.append(full_path)
        else:
            if bool_include_file is True:
                list_paths.append(full_path)
            else:
                pass
    return list_paths


def os_force_remove(file_path: str):
    try:
        os.remove(file_path)
    except OSError as err:
        pass
    finally:
        pass


def os_force_remove_dirs(path: str):
    try:
        os.removedirs(path)
    except OSError as err:
        pass
    finally:
        pass


def secure_random_seed_init():
    random.seed(secrets.randbits(64))
    return True


def fast_random_bytes(bytes_size):
    array = bytearray()
    for i in range(bytes_size):
        array.append(random.randint(0, 255))
    return bytes(array)


def override_random_data(file_path: str):
    file_bytes_size = os.path.getsize(file_path)
    with open(file_path, "wb", buffering=0) as fp:
        write_bytes_size = 0
        while write_bytes_size < file_bytes_size:
            fp.write(fast_random_bytes(SECURE_BLOCK_SIZE))
            write_bytes_size += SECURE_BLOCK_SIZE
        fp.flush()
        fd = fp.fileno()
        os.fsync(fd)
    return


def override_fixed_data(file_path: str, fill_bytes=b'\xff'):
    if type(fill_bytes) is not bytes:
        fill_bytes = b'\xff'
    file_bytes_size = os.path.getsize(file_path)
    with open(file_path, "wb", buffering=0) as fp:
        write_bytes_size = 0
        while write_bytes_size < file_bytes_size:
            for i in range(SECURE_BLOCK_SIZE):
                fp.write(fill_bytes)
            write_bytes_size += SECURE_BLOCK_SIZE
        fp.flush()
        fd = fp.fileno()
        os.fsync(fd)
    return


def write_random_block(root_path: str):
    file_bytes_size = secrets.randbelow(SECURE_BLOCK_SIZE)
    with open(root_path, "wb") as fp:
        fp.write(fast_random_bytes(file_bytes_size))
        fp.flush()
        fd = fp.fileno()
        os.fsync(fd)
    os_force_remove(root_path)
    return


def fill_random_data(file_path: str, fill_size=5 * 1024 * 1024 * 1024):
    with open(file_path, "wb") as fp:
        write_bytes_size = 0
        while write_bytes_size < fill_size:
            fp.write(fast_random_bytes(1))
            write_bytes_size += 1
        fp.flush()
        fd = fp.fileno()
        os.fsync(fd)
    return


def upset_inodes(base_path, count=128):
    base_name = os.path.basename(base_path)
    if base_name == '':
        base_path += 'cleanup'
    cleanup_list = []
    for index in range(count):
        rand_path = '%s.%d.rand' % (base_path, index)
        cleanup_list.append(rand_path)
        write_random_block(rand_path)
    for del_path in cleanup_list:
        os_force_remove(del_path)
    return


def wipe_free_space(base_path: str):
    base_name = os.path.basename(base_path)
    if base_name == '':
        base_path += 'wipe'
    cleanup_list = []
    index = 0
    while True:
        try:
            rand_path = '%s.%d.rand' % (base_path, index)
            cleanup_list.append(rand_path)
            fill_random_data(rand_path)
        except OSError as err:
            # print(err.characters_written)
            break
    for del_path in cleanup_list:
        os_force_remove(del_path)
    return


def secure_delete(base_path: str, count: int=3):
    if count < 1:
        count = 1
    if os.path.exists(base_path) is False:
        return
    if os.path.isdir(base_path):
        file_list = enum_paths(base_path)
        for file_path in file_list:
            secure_delete(file_path,count)
        os_force_remove_dirs(base_path)
    elif os.path.isfile(base_path):
        random_count = count - 1
        for num in range(random_count):
            override_random_data(base_path)
            # override_fixed_data(base_path)
        override_fixed_data(base_path)
        os_force_remove(base_path)
    else:
        os_force_remove(base_path)
    return


if __name__ == '__main__':
    # secure_random_seed_init()
    # print(fast_random_bytes(10))
    # secure_delete('I:\\1.exe')
    # wipe_random_block('I:\\1.exe')
    # wipe_free_space('I:\\')
    pass
