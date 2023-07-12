import os
import shutil


class FileHandler:
    base_path = None
    working_directory = None

    # create a folder in this path
    @staticmethod
    def create_dir(more_path):
        path = os.getcwd()
        os.mkdir(path + more_path)

    @staticmethod
    def add_coomand(adding_path_or_folder):
        # path = FileHandler.find_base_path()
        path_dest = r'C:\Users\User\PycharmProjects\Wit_project\.wit\staging_area'
        print(path_dest)
        print(adding_path_or_folder)
        print("Before copying file:")
        destination = shutil.copytree(adding_path_or_folder, path_dest)
        print(destination)

    # TODO: to get the base path
    @classmethod
    def find_base_path(cls):
        if cls.base_path:
            return cls.base_path
        # TODO: find first dir's path with .wit in it
        found = False
        # TODO: handle not wit repo
        # raise Exception("Not a wit repository")
