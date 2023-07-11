import sys
import os


class FileHandler:
    base_path = None
    working_directory = None

    #create a folder in this path
    @staticmethod
    def create_dir(more_path):
        path = os.getcwd()
        os.mkdir(path+more_path)


#פה לא עשיתי עדיין כלום אבל צריך לדעת איך מביאים את הניתוב
    @classmethod
    def find_base_path(cls):
        if cls.base_path:
            return cls.base_path
        # TODO: find first dir's path with .wit in it
        found = False
        # TODO: handle not wit repo
        # raise Exception("Not a wit repository")



    # @classmethod
    # def validate_path(cls, path):
    #     full_path = os.path.join(cls.working_directory, path)
    #     if not os.path.exists(full_path):
    #         pass
    #         # TODO: handle file doesn't exist
    #
    # @classmethod
    # def copy_item(cls, origin, target):
    #     pass

class Wit:
    @staticmethod
    def validate_is_wit_repo():
        #כאן הוא צריך להחזיר את הניתוב
        return FileHandler.find_base_path()
    @staticmethod
    def init():
        print("hi i'm in the init")
        if Wit.validate_is_wit_repo():
            #אם הניתוב שהוא העתיק ריק אז צריך לעשות משו ואם לא אז רק להוסיף
            pass
        else:
            FileHandler.create_dir(r"\.wit")
            FileHandler.create_dir(r"\.wit\staging_area")
            FileHandler.create_dir(r"\.wit\images")

    @staticmethod
    def add(args):
        pass

    @staticmethod
    def commit(args):
        pass


class WitInterface:
    @staticmethod
    # find the command and run the function
    def handle_commands(command, args):
        if command == "init":
            Wit.init()
        elif command == "add":
            Wit.add(args)
        else:
            Wit.commit(args)


if __name__ == "__main__":
    command = sys.argv[1]
    args = sys.argv[2:]
    WitInterface.handle_commands(command, args)
