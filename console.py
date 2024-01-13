#!/usr/bin/python3
"""This module defines the entry point of the command interpreter."""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """The command interpreter."""
    prompt = "(hbnb)"
    _classes = ["BaseModel"]

    def emptyline(self):
        """Do nothing  an empty line."""
        pass
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_create(self, arg):
        """ create new instance"""

        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self._classes:
            print("** class doesn't exist **")
        else:
            new_ins = BaseModel()
            new_ins.save()
            print(new_ins.id)

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
            object = storage.all()
            pass



                
    def do_EOF(self, line):
        """EOF signal to exit the program."""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
