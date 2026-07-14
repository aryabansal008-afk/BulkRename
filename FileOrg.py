import os

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)
    i=1
    for file in files_with_ext:
        os.rename(file, f"FileOrg_{i}{ext}")
        i +=1

if __name__ == "__main__": # It tells Python: "Run this code only if this file is executed directly, not if it is imported into another Python file."
    files = os.listdir()
    arrange_files(files,".jpg")

print(os.getcwd())