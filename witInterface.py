from wit import Wit
class WitInterface:

    # find the command and run the function
    @staticmethod
    def handle_commands(command, args):
        if command == "init":
            Wit.init()
        elif command == "add":
            Wit.add(args[0])
        else:
            Wit.commit(args)