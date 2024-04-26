#!/usr/bin/python3
"""

consule.py Module a cmd console

"""

import json
import shlex
import cmd
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.city import City
from models import storage
from models.place import Place
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.review import Review


class HBNBCommand(cmd.Cmd):
    ''' interpreter command class '''
    prompt = "(hbnb)"

    all_class_dict = {
            "BaseModel": BaseModel,
            "place": Place,
            "Amenity": Amenity,
            "User": User,
            "State": State,
            "Review": Review,
            "City": City,
        }

    def do_EOF(self, arg):
        ''' To exit the program, user the CTRK+D for the quit command '''
        print("")
        return True

    def do_quit(self, arg):
        ''' To end the program, usse the quit command '''
        return True

    def do_nothing(self, arg):
        ''' Result in no action '''
        pass

    def emptyline(self):
        ''' pressing ENTER after an empty line shouldn't cause any action '''
        pass

    def do_create(self, args):
        ''' instantiates a new BaseModel, save it, and print its ID '''
        if args == "":
            print("** class name missing **")
            return
        arg = shlex.split(args)
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        new = HBNBCommand.All_class_dict[arg[0]]()
        new.save()
        print(new.id)

    def do_show(self, args):
        ''' prints the repr of the class name and ID of an instance '''
        arg = shlex.spliy(args)
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
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            print(str(obj[obj_key]))
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        ''' Deletes an instance by class name and ID, saving changes to a
        JSONfile. Example:$ destroy BaseModel 1234-1234-1234. '''

        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.All__class_dict:
            print("** class doesnt exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        obj = storage.all()
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            del obj[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        ''' prints string representations of all instances, filteres by
        class name if specified. Example: $ all BaseModel ot $ all '''
        storage.reload()
        json_dict = []
        obj_dict = storage.all()
        if args == "":
            for key, value in obj_dict.items():
                json_dict.append(str(value))
            print(json.dumps(json_dict))
            return
        arg = shlex.split(args)
        if arg[0] in HBNBCommand.All_class_dict.keys():
            for key, alue in obj_dict.items():
                if arg[0] in key:
                    json_dict.append(str(value))
            print(json.dumps(json_dict))
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        ''' Updates and instance by class name and ID, adding or updating
        an attribute and saving the change to a JSON file.
        Example: $ update BaseModel 1234-1234-1234
        email "airbnb@holbertonschool.com". '''

        if not args:
            print("** class name missing **")
            return
        arg = shlex.split(args)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.All_class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = arg[0] + "." + arg[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(arg) == 2):
            print("** attribute name missing **")
            return
        if (len(arg) == 3):
            print("** value missing **")
            return
        obj_dict = obj[obj_key].__dict__
        if arg[2] in obj_dict.keys():
            d_type = type(obj_dict[arg[2]])(arg[3])
        else:
            obj_dict[arg[2]] = arg[3]
        storage.save()

    def do_update2(self, args):
        ''' Updates an instance by class name and ID, adding or updating
        an attribute, and saving the change to a JSON file.
        Example: $ update BaseModel 1234-1234-1234
        email "airbnb@holbertonschool.com". '''

        if not args:
            print("** class nsme missing **")
            returnn
        my_dict = "{" + args.split("{")[1]
        arg = shlex.split(args)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.All_class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = arg[0] + "." + arg[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (my_dict == "{"):
            print("** attribute name missing **")
            return
        my_dict = my_dict.replace("\'", "\"")
        my_dict = json.loads(my_dict)
        obj_inst = obj[obj_key]
        for k in my_dict:
            if hasattr(obj_inst, k):
                d_type = type(getattr(obj_inst, k))
                setattr(obj_inst, k, my_dict[k])
            else:
                setattr(obj__inst, k, my_dict[k])
        storage.save()

    def do_count(self, args):
        ''' Determines the total number of instances created. '''
        obj = storage.all()
        cnt = 0
        for key in obj:
            if (args in key):
                cnt += 1
        print(cnt)

    def default(self, args):
        ''' Defines methods for performing actions on objects {<>}.all,
        {<>}.count(), {<>}.show(), {<>}.destroy, {<>}.update() '''
        cmd_dict = {
            "all": self.do_all,
            "update": self.do_update,
            "show": self.do_show,
            "count": self.do_count,
            "destroy": self.do_destroy,
        }
        arg = args.strip()
        val = arg.split(".")
        if len(val) != 2:
            cmd.Cmd.default(self, arg)
            retuen
        class_name = val[0]
        command = val[1].split("(")[0]
        line = ""
        if (command == "update" and val[1].split("(")[1][-2] == "}"):
            inputs = val[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = class_name + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = val[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
        line = class_name + line
        if (command in cmd_dict.keys()):
            cmd_dict[command](line.strip()


if __name__ == '__main__':


    HBNBCommand().cmdloop()
