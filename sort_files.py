from pathlib import Path
import os
import shutil


folder = Path.home() / "Downloads"
# Create subfolders in the Downloads directory to organize files
subfolders = ["CSV_Files", "PDF_Files", "Video_Files", "Installers", "ZIP_archives", "Other"]

for subfolder in subfolders:
    try:
      os.makedirs(folder / subfolder)
    except FileExistsError:
      print(f"{subfolder} is already created")


for filename in os.listdir(folder):
    full_path = folder / filename
    if filename.endswith(".csv"):
        shutil.move(full_path, folder / "CSV_Files" / filename)
    elif filename.endswith(".pdf"):
        shutil.move(full_path, folder / "PDF_Files" / filename)
    elif filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".webm"):
       shutil.move(full_path, folder / "Video_files" / filename)
    elif filename.endswith(".exe") or filename.endswith(".msi"):
        shutil.move(full_path, folder / "Installers" / filename)
    elif filename.endswith(".zip") or filename.endswith(".rar"):
        shutil.move(full_path, folder / "ZIP_archives" / filename)
    elif filename.endswith(".eml") or filename.endswith("docx") or filename.endswith("xml") or filename.endswith("dotx"):
        shutil.move(full_path, folder / "Other" / filename)
print("Files sorted successfully.")
