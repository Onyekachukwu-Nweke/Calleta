#!/usr/bin/python3
" Console application for Calleta"
import cmd
import sys
# from dotenv import dotenv_values
import models
from models.basemodel import BaseModel, Base
from models.user import User
# from models.cart import Cart
from models.payment import Payment
from models.order import Order
from models.orderitem import OrderItem
from models.product import Product
from models.category import Category
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "Category": Category, "OrderItem": OrderItem,
           "Product": Product, "Payment": Payment, "Order": Order}
env_vars = dotenv_values('.env')

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
    
    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    Calleta().cmdloop()