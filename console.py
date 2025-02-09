#!/usr/bin/python3
""" This is the Console for AirBnB CLone v2 """
import cmd
import sys
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = "(hbnb) "
    all_classes = {"BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"}

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            if args[0] not in self.all_classes:
                raise NameError()
            obj = eval(args[0] + '()')
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        else:
            pairs = [s.split('=', maxsplit=1) for s in args[1:] if '=' in s]
            for key, value in pairs:
                try:
                    setattr(obj, key, int(value))
                except ValueError:
                    try:
                        setattr(obj, key, float(value))
                    except ValueError:
                        try:
                            setattr(obj, key, str(value).replace('_', ' '))
                        except ValueError:
                            pass
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            if args[0] not in self.all_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            objects = storage.all()
            key = args[0] + '.' + args[1]
            obj = objects[key]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            if args[0] not in self.all_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            objects = storage.all(eval(args[0]))
            key = args[0] + '.' + args[1]
            obj = objects[key]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        else:
            obj.delete()
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        Exceptions:
            NameError: when there is no object taht has the name
        """
        try:
            if not line:
                objects = storage.all()
            else:
                args = split(line)
                if args[0] not in self.all_classes:
                    raise NameError()
                objects = storage.all(eval(args[0]))
        except NameError:
            print("** class doesn't exist **")
        else:
            my_list = []
            for key in objects:
                my_list.append(objects[key])
            print(my_list)

    def do_update(self, line):
        """Updates an instanceby adding or updating attribute
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            if args[0] not in self.all_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            objects = storage.all()
            key = args[0] + '.' + args[1]
            if key not in objects:
                raise KeyError()
            if len(args) < 3:
                raise AttributeError()
            if len(args) < 4:
                raise ValueError()
            obj = objects[key]
            try:
                setattr(obj, args[2], eval(args[3]))
            except Exception:
                setattr(obj, args[2], args[3])
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")
        else:
            obj.save()

    def count(self, line):
        """count the number of instances of a class
        """
        counter = 0
        try:
            args = split(line)
            if args[0] not in self.all_classes:
                raise NameError()
        except NameError:
            print("** class doesn't exist **")
        else:
            objects = storage.all(eval(args[0]))
            print(len(objects))

    def strip_clean(self, args):
        """strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns
        """
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        """retrieve all instances of a class and
        retrieve the number of instances
        """
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
