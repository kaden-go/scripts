import os
import shutil
import time

download_dir = "/Users/kaden/Downloads/"

class DownloadSorter():

    def __init__(self, download_dir):
        self.__download_dir = download_dir

    def get_file_list(self):
        files = os.listdir(self.__download_dir)
        return files

    def create_folder(self, name):
        if not os.path.exists(self.__download_dir + name):
            os.mkdir(self.__download_dir + name)

    def move_file(self, file_name, file_extension_folder):
        print(self.__download_dir + file_name + "->" + self.__download_dir + file_extension_folder + "/" + file_name)
        shutil.move(self.__download_dir + file_name, self.__download_dir + file_extension_folder + "/" + file_name)
        
if __name__ == "__main__":
    sorter = DownloadSorter(download_dir)
    
    while(1):

        files = sorter.get_file_list()

        for file in files:
            # do not move hidden files
            if not file[0] == '.': 

                # do not move folders
                if not os.path.isdir(download_dir + file):
                    extension = os.path.splitext(file)[1] 

                    # create folder for each file extension
                    sorter.create_folder(extension[1:])

                    # move file into respective folder
                    sorter.move_file(file, extension[1:])

        time.sleep(1)