<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/Oliveth96/AirBnB_clone_v2/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/Oliveth96/AirBnB_clone_v2/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/__init__.py) [/models/base_model.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/base_model.py) | Defines a class to manage persistent file storage system|

| 7. Create User class | 
[/models/engine/file_storage.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/engine/file_storage.py) [/models/user.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/user.py) | Dynamically implements a user class |
| 8. More Classes | [/models/user.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/user.py) [/models/place.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/place.py) [/models/city.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/city.py) [/models/amenity.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/amenity.py) [/models/state.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/state.py) [/models/review.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/review.py) | Dynamically implements more classes |

|10. 0-setup_web_static.sh | (https://github.com/Oliveth96/AirBnB_clone_v2/0-setup_web_static.sh) | A Bash script that sets up your web servers for the deployment of web_static|


<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

