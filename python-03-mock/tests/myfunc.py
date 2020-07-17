import os

def check_dir_exists(dir_path):
    pass

def check_file_exists(file_path):
    pass

def create_file(dst_dir, file_name):
    if check_dir_exists(dst_dir) and not check_file_exists(file_name):
        file_path = os.path.join(dst_dir, file_name)
        with open(file_path, "w") as f:
            f.write("")
        return True
    return False

def delete_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)