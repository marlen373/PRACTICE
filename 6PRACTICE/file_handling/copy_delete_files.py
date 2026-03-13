import os
import shutil
shutil.copy("sample.txt", "sample_backup.txt")
print("copied")

if os.path.exists("sample_backup.txt"):
    os.remove("sample_backup.txt")