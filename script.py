
import os
import random
import shutil
import string

from pathlib import Path
from datetime import datetime

SOURCE_DIR = "/Users/luis/Documents/03 Personal/Personal/images/to_rename/2025_06_07"
DEST_DIR = "/Users/luis/Documents/03 Personal/Personal/images/to_rename/ordered"

def random_token(length=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def format_date_folder(name):
    try:
        return datetime.strptime(name, "%B %d, %Y")
    except ValueError:
        return None

def main():
    # import pdb
    # pdb.set_trace()

    source_path = Path(SOURCE_DIR)
    dest_path = Path(DEST_DIR)
    ensure_dir(dest_path)

    token = random_token()

    for folder in source_path.iterdir():
        if folder.is_dir():
            date_obj = format_date_folder(folder.name)
            # This is to skip folders that don't follow the naming format
            if not date_obj:
                continue  
            
            month_folder_name = f"{date_obj.strftime('%B %Y')}"
            month_folder_path = dest_path / month_folder_name
            ensure_dir(month_folder_path)

            # Copy and rename each image in the folder
            for idx, img_file in enumerate(folder.glob("*.*")):
                if img_file.is_file():
                    ext = img_file.suffix
                    counter = f"{idx+1:03d}"  # 3-digit padded counter
                    new_name = f"{date_obj.strftime('%Y-%m-%d')}_{counter}_{token}{ext}"
                    shutil.copy2(img_file, month_folder_path / new_name)
                    print(f"Copied: {img_file.name} -> {month_folder_name}/{new_name}")

if __name__ == "__main__":
    main()
