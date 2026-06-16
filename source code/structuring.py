import os
import shutil

desktop = r"C:\Users\surya\Desktop"
documents = r"C:\Users\surya\Documents"

destination = r"C:\Users\surya\Organized_Files"

# File categories
categories = {
    ".pdf": "Documents/PDF",
    ".docx": "Documents/Word",
    ".doc": "Documents/Word",
    ".xlsx": "Documents/Excel",
    ".xls": "Documents/Excel",
    ".pptx": "Documents/PPT",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".exe": "Software",
    ".msi": "Software",
    ".py": "Code/Python",
    ".html": "Code/HTML",
    ".css": "Code/HTML",
    ".js": "Code/JavaScript"
}

def safe_move(src, dst):
    try:
        if os.path.exists(dst):
            base, ext = os.path.splitext(dst)
            counter = 1
            while os.path.exists(f"{base}_{counter}{ext}"):
                counter += 1
            dst = f"{base}_{counter}{ext}"

        shutil.move(src, dst)
        print(f"Moved: {src}")
    except Exception as e:
        print(f"Failed: {src} -> {e}")

def organize(folder):
    for item in os.listdir(folder):
        path = os.path.join(folder, item)

        # Move folders
        if os.path.isdir(path):
            target = os.path.join(destination, "Folders")
            os.makedirs(target, exist_ok=True)
            safe_move(path, os.path.join(target, item))

        # Move files
        elif os.path.isfile(path):
            ext = os.path.splitext(item)[1].lower()
            category = categories.get(ext, "Others")

            target = os.path.join(destination, category)
            os.makedirs(target, exist_ok=True)

            safe_move(path, os.path.join(target, item))

organize(desktop)
organize(documents)

print("Organization completed!")