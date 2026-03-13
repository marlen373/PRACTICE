import shutil
import os

os.makedirs("folderA", exist_ok=True)
os.makedirs("folderB", exist_ok=True)


with open("folderA/sample.txt", "w") as f:
    f.write("This is a test file")


shutil.copy("folderA/sample.txt", "folderB/sample.txt")



shutil.move("folderB/sample.txt", "folderB/moved_sample.txt")

