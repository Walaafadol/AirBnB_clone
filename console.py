#!/usr/bin/python3
"""This module defines the entry point of the command interpreter."""

import cmd
import shlex
from models.base_model import BaseModel
import re
from models.user import User
from models import storage




class HBNBCommand(cmd.Cmd):
    """The command interpreter."""
    prompt = "(hbnb)"
    _classes = ["BaseModel", "User"]

    def emptyline(self):
        """Do nothing  an empty line."""
        pass
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    

    def do_create(self, arg):
        """ Create a new instance """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self._classes:
            print("** class doesn't exist **")
        else:
            new_inst = eval(f"{commands[0]}()")
            storage.save()
            print(new_inst.id)
    def do_show(self, arg):
        """ Display the string representation of a class instance"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self._classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self._classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ print representation of all instance"""
        objects = storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self._classes:
                print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                        print(str(value))

    def do_update(self, arg):
        """update an istance"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self._classes:
            print("** class doesn't exist **")
        elif len(commands) > 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])

            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obje = objects[key]
                attrname = commands[2]
                attvalue = commands[3]
                try:
                    attvalue = eval(attvalue)
                except Exception:
                    pass
                setattr(obje, attrname, attvalue)
                obje.save()



                
    def do_EOF(self, line):
        """EOF signal to exit the program."""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
