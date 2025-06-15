This is a simple, extensible, and non-recursive file organizer written in Python that helps you sort and categorize files in a given directory based on their extensions.

What It Does
1. Organizes all files directly inside a specified directory (non-recursively).
2. Moves files into categorized subfolders (like Images, Documents, Videos, etc.).
3. Prevents accidental overwrites by ensuring unique filenames during the move.
4. Supports a wide range of file extensions and gracefully handles unknown types by placing them into an Others folder.

How It Works
1. The script prompts the user to enter a target directory.
2. It scans only the top-level files in that directory.
3. Based on file extensions, it moves files into predefined folders like:
   a. .jpg, .png → Images/
   b. .mp4, .avi → Videos/
   c. .exe, .dll → Executables/, Dynamic Link Libraries/
4. If two files have the same name in the same category, the script auto-renames with (1), (2), etc., to avoid overwriting

Supported Extensions (Customizable)
The script currently maps over 20 file types including:
1. Images (.jpg, .png, .gif)
2. Documents (.pdf, .docx, .txt)
3. Videos (.mp4, .avi)
4. Code (.cpp, .py, .c)
5. Libraries (.dll, .lib, .so)
6. Archives (.zip, .rar)
7. Audio (.mp3, .wav)
📍 You can easily customize the extension-folder mapping in the folder_dictionary to meet your requirements too

How to Run
     _python file_organizer.py_
Then enter the absolute or relative path to the folder you want to organize.

Why Non-Recursive?
The script is intentionally designed to only process top-level files, so re-running it won't create nested folders like Images/Images/xyz.jpg.

Future Ideas (Optional Enhancements)
1. Add recursive mode as a flag.
2. Support for config file or CLI arguments.
