#!/usr/bin/python3
"""Command interpreter module"""

import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        new_instance = storage.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        print(instances[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        del instances[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        instances = storage.all()

        if not args:
            print([str(inst) for inst in instances.values()])
            return

        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        filtered_instances = [str(inst) for inst in instances.values() if inst.__class__.__name__ == class_name]
        print(filtered_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        value = args[3]
        try:
            value = eval(value)
        except:
            pass

        setattr(instances[key], attribute_name, value)
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
