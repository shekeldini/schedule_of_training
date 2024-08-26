import os


def get_path(path):
    if not os.path.exists(path):
        return get_path("../" + path)
    return path
