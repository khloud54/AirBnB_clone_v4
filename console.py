#!/usr/bin/python3
import cmd
import shlex
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models import storage
from models.state import State
from datetime import date time
from models.engine.file_storage import FileStorage

"""
program called console.py that contains the entry point of the command
interpreter.
"""

class HBNBCommand(cmd.Cmd):
    ''' a command interpreter class '''
    prompt = "(hbnb)"

    All_class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
    }

    def do_EOF(self, arg):
        """
        EOF (ctrl+D) signal to exit the program.

        """
        print ("")
        return True

    def do_quit(self, arg):
        ''' Quit command to exit the program '''
        return True

    def do_nothing(self, arg):
        ''' does nothing '''
        pass

    def emptyline(self):
        """
        Do nothing when an empty line is entered.

        """
        pass

    def do_create(self, arg):
        ''' Creates a new instance BaseModel, saves prints its id '''
        if args == '':
            print("** class name missing **")
            return
        arg = shlex.split(args)
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        new = HBNBCommand.All_class_dict[arg[0]]()
        new.save()
        print(new.id)

        def do_show(self, arg):
            """ 
            show the string representation of an instance.
            Usage: show <class_name> <id>
            """
            commands = shlex.split(arg)

            if len(commands) == 0:
                print("** class name missing **")
            elif commands[0] not in self.valid_classes:
                print("** class doesn,t exist **")
            elif len(commands) < 2:
                print("** instance id missing **")
            else:
                objects = storage.all()

                key = "{}.{}".format(commands[0], commands[1])
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")

        def do_destroy(self, args):
            '''Deletes an instance based on the class name and id.
            Usage: destroy <class_name> <id>'''

            arg = shlex.split(args)
            if len(arg) == 0:
                print("** class name missing **")
                return
            if arg[0] not in HBNBCommand.All_class_dict:
                print("** class doesn't exist **")
                return
            if len(arg) < 2:
                print("** instance id missing **")
                return
            storage.reload()
            obj = storage.all()
            obj_key in obj:
            if obj_key in obj:
                del obj[obj_key]
                storage.save()
            else:
                print("** no instance found **")

        def do_all(self, args):
            ''' prints all string representation of all instances based or not
            on the class name. Ex: $ all BaseModel or $ all '''
            storage.reload()
            json_dict = []
            obj_dict = storage.all()
            if args == '':
                for key, value in obj_dict.items():
                    json_dict.append(str(value)))
                print(json.dumps(json_dict))
                return
            arg = shlex.split(args)
            if arg[0] in HBNBCommand.All_class_dict.keys():
                for key, value in obj_dict.items():
                    if arg[0] in key:
                        json_dict.append(str(value))
                print(json.dumps(json_dict))
                return
            else:
                print("** class doesn't exist **")

        def do_count(self, args):
            ''' counts number of instances of a class
            usage: <class name>.count()
            '''
            objects = storage.all()
            cnt = 0
            for key in obj:
                if (args in key):
                    cnt += 1
            print(cnt)
