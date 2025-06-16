import os
import shutil
import traceback

# Class handling the Organizing
class FileOrganizer:
    def __init__(self,work_dir):

        # This directory is entered by the user to work on
        self.dir_path = work_dir.strip()

        # Add your file extension here to split into the folders
        # 'extension' : 'folder to be mapped to'
        self.folder_dictionary = {
            '.pdf':'PDFs','.png':'Images','.jpg':'Images','.jpeg':'Images','.gif':'Images',
            '.doc':'Documents','.docx':'Documents','.txt':'Documents',
            '.csv':'data','.xlsx':'data',
            '.zip':'archives','.rar':'archives',
            '.exe':'Executables',
            '.mp3':'Music','.wav':'Music',
            '.mp4':'Videos','.avi':'Videos','.flv':'Videos','.wmv':'Videos',
            '.cpp':'CPP Files',
            '.py':'Python Files',
            '.c':'C Files',
            '.dll' : 'Dynamic Link Libraries',
            '.lib' : 'Library Files',
            '.so' : 'Shared Library Objects',
            '.pdb' : 'Program Database Files'
        }

    # The folder entered by the user is processed here
    # Note : All the files in the specified folder are processed here without going into the child folders
    def organize_folder(self):
        try:
            for root,dirs,files in os.walk(self.dir_path):
                for file in files:
                    if root == self.dir_path:
                        self.organize_file(os.path.join(root,file))
        except Exception as e:
            print(f'Exception Occured : {type(e).__name__}')
            print(f'Exception Message : {e}')
            traceback.print_exc()

    # To make sure none of the files that are sent to the organized folder repolaces the existing files.
    def get_unique_filename(self, target_file):
        file_name,ext = os.path.splitext(target_file)
        counter = 1
        while os.path.exists(target_file):
            target_file = f"{file_name}({counter}){ext}"
            counter += 1
        return target_file

    # This is where moving occurs using shutil after generating a proper unique name to be moved into.
    def organize_file(self,file_path):
        try:
            file_name = os.path.basename(file_path)
            file_extension = os.path.splitext(file_name)[1].lower()
            map_folder = self.folder_dictionary.get(file_extension, "Others")

            target_directory = os.path.join(self.dir_path,map_folder)
            os.makedirs(target_directory, exist_ok=True)

            dest_path = self.get_unique_filename(os.path.join(target_directory,file_name))
            shutil.move(file_path,dest_path)
            print(f"Moved file {file_path} to {dest_path}")
        except Exception as e:
            print(f'Exception Occured : {type(e).__name__}')
            print(f'Exception Message : {e}')
            traceback.print_exc()

if __name__ == '__main__':

    # This prompts the user to input the path
    input_directory = input("Enter the directory to be sorted : ")
    organizer = FileOrganizer(input_directory)
    organizer.organize_folder()