import os
import shutil

folder = input("Enter folder path to organize: ")
extensions = {
    "images":
[".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt"],
    "videos": [".mp4", ".avi", ".mkv"]
}

for filename in os.listdir(folder):
    for category, exts in extensions.items():
        for ext in exts:
            if filename.endswith(ext):
                dest = os.path.join(folder, category)
                os.makedirs(dest, exist_ok=True)
                shutil.move(os.path.join(folder, filename), 
                            os.path.join(dest, filename)
                        )
                print(f"Moved {filename} to {category}")