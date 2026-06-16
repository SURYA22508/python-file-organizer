# Python File Organizer

Ever opened your Desktop and wondered:

"How did it become this messy?"

PDFs mixed with screenshots.
ZIP files buried between documents.
Python scripts hiding somewhere you can't find.

Instead of organizing everything manually, I built a Python script to do it automatically.

---

## What It Does

This script scans your Desktop and Documents folders and automatically organizes files into structured categories.

For example:

Desktop/
├── resume.pdf
├── project.zip
├── image.png
├── script.py

Becomes:

Organized_Files/
├── Documents/
│   └── PDF/
│       └── resume.pdf
├── Archives/
│   └── project.zip
├── Images/
│   └── image.png
├── Code/
│   └── Python/
│       └── script.py

---

## Features

✅ Automatic file categorization

✅ Dynamic folder creation

✅ Duplicate filename handling

✅ Organizes both Desktop and Documents

✅ Supports multiple file formats

✅ Simple and lightweight

---

## Supported Categories

| Category | Extensions |
|-----------|------------|
| PDF | .pdf |
| Word | .doc, .docx |
| Excel | .xls, .xlsx |
| PowerPoint | .pptx |
| Images | .jpg, .jpeg, .png, .gif |
| Videos | .mp4, .mov |
| Archives | .zip, .rar |
| Software | .exe, .msi |
| Python | .py |
| HTML/CSS | .html, .css |
| JavaScript | .js |
| Others | Unsupported formats |

---

## Why I Built This

I wanted to improve my Python skills while solving a real problem.

Instead of following another tutorial, I chose to automate a task I actually face.

This project helped me practice:

- File Handling
- Directory Management
- Python Automation
- Error Handling
- Working with OS and Shutil modules

---

## Technologies Used

- Python
- os
- shutil

---

## Future Improvements

- GUI version using Tkinter
- Select custom folders
- Undo functionality
- Activity logs
- Organize files by date
- AI-powered file categorization

---

## Installation

```bash
git clone https://github.com/yourusername/smart-file-organizer.git
