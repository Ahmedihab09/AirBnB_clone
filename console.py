#!/usr/bin/python3


"""Entry point of the command interpreter"""

import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):

    """Defines the Command Interpreter."""

    prompt = "(hbnb)"
    classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
        ]

    def do_EOF(self, arg):
        """ EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def emptyline(self):
        """ Empty line - Not execute anything"""
        pass

    def _get_class_instance(self, class_name):
        """Get an instance of a class based on its name"""
        class_to_create = globals().get(class_name)
        if class_to_create:
            return class_to_create()
        print(f"Class '{class_name}' not found in globals()")
        return None

    def _print_instances(self, class_name):
        """Print instances based on the class name"""
        instances = storage.all()
        if not class_name or class_name in HBNBCommand.classes:
            print([str(inst) for inst in instances.values()])
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")

    def do_create(self, arg):
        """ Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_instance = self._get_class_instance(arg)
        if new_instance:
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name and id """
        a = arg.split()
        if not arg:
            print("** class name missing **")
        elif a[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(a) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(a[0], a[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(a[0], a[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on
        the class name and id"""
        a = arg.split()
        if not arg:
            print("** class name missing **")
        elif a[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(a) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(a[0], a[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(a[0], a[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation
        of all instances
        based or not on the class name"""
        a = arg.split()
        self._print_instances(
            a[0] if a and a[0] in HBNBCommand.classes else None
            )

    def do_count(self, arg):
        """retrieve the number of instances of a class"""
        count = 0
        a = arg.split()
        for v in storage.all().values():
            if a[0] == v.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
