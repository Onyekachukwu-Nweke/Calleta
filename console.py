#!/usr/bin/python3
" Console application for Calleta"
import cmd
import sys
# from basemodel import BaseModel
import shlex


class Calleta(cmd.Cmd):
    """
    Core functionality of the Calleta console app
    """
    prompt = '(cale) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    Calleta().cmdloop()