import os


def get_top_directory():
    import akanda
    return akanda.__path__[0]


def get_test_module():
    module = os.path.basename(get_top_directory())
    return module.replace("/", ".")
