import sys
from witInterface import WitInterface


if __name__ == "__main__":
    try:
        command = sys.argv[1]
        args = sys.argv[2:]
        WitInterface.handle_commands(command, args)
    except:
        print("gmvk")
