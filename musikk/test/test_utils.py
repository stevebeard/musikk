import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import pathlib

def get_test_filepath(filename):
    return os.path.join(dir_path, filename)

def get_test_file_uri(filename):
    filepath = get_test_filepath(filename)
    return pathlib.Path(filepath).as_uri()