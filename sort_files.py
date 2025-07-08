from pathlib import Path
import os
import shutil


folder = Path.home() / "Downloads"
# Create subfolders in the Downloads directory to organize files
subfolders = ["CSV_Files", "PDF_Files", "Video_Files", "Installers", "ZIP_archives"]

for subfolder in subfolders:
    try:
      os.makedirs(folder / subfolder)
    except FileExistsError:
      print(f"{subfolder} is already created")


for filename in os.listdir(folder):
    full_path = folder / filename
    if filename.endswith(".csv"):
        shutil.move(full_path, folder / "CSV_Files" / filename)
    if filename.endswith(".pdf"):
        shutil.move(full_path, folder / "PDF_Files" / filename)
    if filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".webm"):
       shutil.move(full_path, folder / "Video_files" / filename)
    if filename.endswith(".exe") or filename.endswith(".msi"):
        shutil.move(full_path, folder / "Installers" / filename)
    if filename.endswith(".zip") or filename.endswith(".rar"):
        shutil.move(full_path, folder / "ZIP_archives" / filename)

print("Files sorted successfully.")