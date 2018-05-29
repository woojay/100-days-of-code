import os
import platform
import subprocess

import cat_services as cat


def print_header():
    print('---------------------------')
    print('    LOLCat Factory APP')
    print('---------------------------')
    print()


def get_or_create_output_folder():

    folder = 'cats'
    base_folder = os.path.dirname(__file__)
    full_path = os.path.abspath(os.path.join(base_folder, folder))

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating', folder, 'folder')
        os.mkdir(full_path)
    else:
        print('Found', folder, 'folder')

    return full_path


def download_cats(folder):

    cat_count = 4

    for i in range(1, cat_count+1):
        name = 'lolcat_{}'.format(i)
        cat.get_cat(folder, name)
        print('Downloaded', name)


def display_cats(folder):

    system = platform.system()

    if system == 'Dwarwin':
        subprocess.call(['open', folder])
    elif system == 'Windows':
        subprocess.call(['explorer', folder])   # or 'start'
    elif system == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("Current OS not supported.")

def main():

    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


if __name__ == '__main__':
    main()
