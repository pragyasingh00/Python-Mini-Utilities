import os
import shutil

# ✅ Ask user to input the folder path
source_folder = input("Enter the full path of the folder you want to organize:\n").strip()

# ✅ Validate if the folder exists
if not os.path.exists(source_folder):
    print(f"\n❌ The folder '{source_folder}' does not exist.")
    exit()

# ✅ Loop through each file in the folder
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    # ✅ Skip if it's a folder
    if os.path.isdir(file_path):
        continue

    # ✅ Extract file extension
    _, extension = os.path.splitext(filename)
    extension = extension[1:].lower()  # remove dot and lowercase

    # ✅ Handle files with no extension
    if not extension:
        extension = "no_extension"

    # ✅ Make destination folder based on extension
    destination_folder = os.path.join(source_folder, extension)
    os.makedirs(destination_folder, exist_ok=True)

    # ✅ Move file into the right folder
    destination_path = os.path.join(destination_folder, filename)
    shutil.move(file_path, destination_path)

    print(f"✅ Moved: {filename} → {extension}/")

print("\n🎉 All files organized successfully!")
