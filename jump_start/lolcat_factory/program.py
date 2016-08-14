import os
import platform
import subprocess

from jump_start.lolcat_factory import cat_service


def main():
    print_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('-----------------------------------')
    print('         LOLCAT FACTORY')
    print('-----------------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    # full_path = os.path.abspath(os.path.join('.', folder))
    # independent of cwd
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)

    print('Done')


def display_cats(folder):
    # windows explorer 'start. ' mac 'open'
    print('Displaying cats in Windows.')
    if platform.system() == 'Darwin':
        subprocess.call('open')
    elif platform.system() == 'Windows':
        # subprocess.call(['explorer', folder])
        subprocess.call(['start', folder], shell=True)
    elif platform.system() == 'Linux':
        subprocess.call(['xdg.open', folder])
    else:
        print(platform.system() + " OS Not supported")


if __name__ == '__main__':
    main()
