import os, shutil
import zipfile

__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

def clear_cache():
    path = 'cache'
    cache_exists = os.path.isdir('./cache')
    
    if cache_exists:
        folder = './cache'

        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as exception:
                print('Failure to remove %s. Reason: %s' % (file_path, exception))
    else:
        try:
            os.mkdir(path)
        except OSError:
            print('Failure to create directory %s.' % path)


def cache_zip(zip_file_path: str, cache_dir_path: str):
    clear_cache()
    is_a_zipfile = zipfile.is_zipfile(zip_file_path)

    if is_a_zipfile:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_reference:
            zip_reference.extractall(cache_dir_path)


def cached_files():
    directory = '/cache'

    all_files = [os.path.abspath(f'cache/{f}') for f in os.listdir(directory)]

    return all_files


def find_password(file_paths: list):
    """takes the list of file paths from cached_files as an argument. This function should read the text 
    in each one to see if the password is in there. Surely there should be a word in there to incidicate 
    the presence of the password? Once found, find_password should return this password string."""


if __name__ == '__main__':
    cache_zip('data.zip', 'cache')

    file_paths = cached_files()

    