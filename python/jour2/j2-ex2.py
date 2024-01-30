import os

def listFiles(path):
    dir_list = os.listdir(path)

    for item in dir_list:
        item_path = os.path.join(path, item)
        size = os.path.getsize(item_path) if os.path.isfile(item_path) else None
        print(f"{item} - {size} o")

listFiles("/bin")
