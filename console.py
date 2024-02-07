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

        def do_update(self, args):
            """
            update an instance by adding or updating an attribute.
            Usage: update <class_name> <id> <attribute_name>
            "attribute_value>"
            """
            commands = shlex.split(arg)

            if len(commands) == 0:
                print("** class name missing **")
            elif commands[0] not in self.valid_classes:
                print("** class doesn't exist **")
            elif len(commands) <2 :
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
                    obj = objects[key]
                    curly_braces = re.search(r"\{(.*?)\}", arg)

                    if curly_braces:
                        try:
                            str_data = curly_braces.group(1)

                            arg_dict = ast.literal_eval("{" + str_data + "}")

                            attribute_names  = list(arg_dict.keys())
                            attribute_values = list(arg_dict.values())
                            try:
                                attr_name1 = attribute_names[0]
                                attr_name1 = attribute_values[0]
                                setattr(obj, attr_name1, attr_value1)
                            except Exception:
                                pass
                            try:
                                attr_name2 = attribute_names[1]
                                attr_value2 = attribute_values[1]
                                setattr(obj, attr_name2, attr_value2)
                            except Exception:
                                pass
                            else:

                                attr_name = commands[2]
                                attr_value = commands[3]

                                try:
                                    attr_value = eval(attr_value)
                                except Exception:
                                    pass
                                setattr(obj, attr_name, attr_value)

                            obj.save()

        def default(self, arg):
            ''' method defines actions on objects {<>}.all(),{<>}.count()
            {<>}.show(), {<>}.destroy(), {<>}.update()'''
            cmd_dict = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update,
                }

            if cmd_met in method_dict.keys():
                if cmd_met != "update":
                    return method_dict[cmd_met]("{} {}".format(cls_nm, e_arg))
                else:
                    if not cls_nm:
                        print("** class name missing **")
                        return
                    try:
                        obj_id, arg_dict = split_curly_braces(e_arg)
                    except Exception:
                        pass
                    try:
                        call = method_dict[cmd_met]
                        return call("{} {} {}".format(cls_nm, obj_id, arg_dict))
                    except Exception:
                        pass
            else:
                print("** Unknown syntax: {}".format(arg))
                return False


    if __name__ == '__main__':
    HBNBCommand().cmdloop()
