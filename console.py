#!/usr/bin/python3
"""This module defines the entry point of the command interpreter."""

import cmd
class HBNBCommand(cmd.Cmd):
    """The command interpreter."""
    prompt = "(hbnb)"
    def do_quit(sel, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """"Inbuilt EOF command """
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
