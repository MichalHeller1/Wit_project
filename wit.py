from fileHandler import FileHandler

class Wit:
    @staticmethod
    def validate_is_wit_repo():
        # כאן הוא צריך להחזיר את הניתוב
        return FileHandler.find_base_path()

    @staticmethod
    def init():
        print("hi i'm in the init")
        if Wit.validate_is_wit_repo():
            # אם הניתוב שהוא העתיק ריק אז צריך לעשות משו ואם לא אז רק להוסיף
            pass
        else:
            FileHandler.create_dir(r"\.wit")
            FileHandler.create_dir(r"\.wit\staging_area")
            FileHandler.create_dir(r"\.wit\images")

    @staticmethod
    def add(args):
        str_path = str(args)
        FileHandler.add_coomand(str_path)

    @staticmethod
    def commit(args):
        pass

