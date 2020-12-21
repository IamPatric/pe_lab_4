import os

def get_files_count(dir: str) -> int:
    s = os.listdir(path=dir)
    d = len(s)
    return d

files_count = get_files_count("C:\pe_lab_4")
print(files_count)