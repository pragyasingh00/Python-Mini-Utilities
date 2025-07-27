---
📂 Easy File Organizer
Hey there! 👋
This is a super simple Python script that helps you organize your messy folders by putting files into separate folders based on their type (like PDFs, images, songs, etc.).
---
😩 Problem
Ever downloaded a bunch of files and your Downloads folder looks like a jungle?
Yeah... same here.
---
✨ Solution
This script looks at each file's extension (like .jpg, .pdf, .mp3)
and automatically moves it into a folder with that name.
So all your files are sorted nicely. No more chaos!
---
✅ How to Use
Open VS Code or any Python editor.

Run this script:
python organizer.py

It will ask you: "Enter folder path:"

Just paste the folder path you want to clean up. Example:
C:/Users/YourName/Downloads

Boom! Your files are now sorted into folders like pdf, jpg, mp3, etc.
---
🔍 Example
Before:
resume.pdf
photo.jpg
song.mp3
notes.txt
---
After:
📁 pdf → resume.pdf
📁 jpg → photo.jpg
📁 mp3 → song.mp3
📁 txt → notes.txt
---
🛠️ What's Inside
file-organizer/
├── organizer.py ← Main script (you run this)
├── sample_files/ ← Some sample files to test with
├── README.md ← You’re reading it now 😄

---
🔧 Tools Used
Python (any version 3.x+)

Modules: os, shutil — don’t worry, they’re already built into Python.

---
Made by pragya singh
