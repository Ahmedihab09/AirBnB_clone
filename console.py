#!/usr/bin/python3
"""Command interpreter module"""

import cmd
import os
import models
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    file_path = "file.json"
    prompt = '(hbnb) '

    classes = ["BaseModel"]

    def __init__(self):
        super().__init__()
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file_path)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print("Available classes:", globals())
            class_to_create = globals().get(arg)
            if class_to_create:
                new_instance = class_to_create()
                new_instance.save()
                print(new_instance.id)
            else:
                print(f"Class '{arg}' not found in globals()")

if __name__ == '__main__':
    HBNBCommand().cmdloop()