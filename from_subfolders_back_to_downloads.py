from pathlib import Path
import os, shutil

downloads_folder = Path.home() / "Downloads"

for root, dirs, files in os.walk(downloads_folder):
    for filename in files:
        if not filename.endswith(".ini"):
            shutil.move(os.path.join(root, filename), downloads_folder)

print(f"reverted all files to {downloads_folder}")