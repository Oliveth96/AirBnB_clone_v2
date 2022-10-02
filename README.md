<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/Oliveth96/AirBnB_clone_v2/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|

| prepare your web browsers | [0-setup_web_static.sh] (https://github.com/Oliveth96/AirBnB_clone_v2/blob/dev/0-setup_web_static.sh) | A Bash script that sets up your web servers for the deployment of web_static

| 2: Generate Archive | [1-pack_web_static.py]
(https://github.com/Oliveth96/AirBnB_clone_v2/blob/dev/1-pack_web_static.py) | Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack |

| 3: Distribute Archive | [2-do_deploy_web_static.py](https://github.com/Oliveth96/AirBnB_clone_v2/blob/dev/2-do_deploy_web_static.py) | A Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy |

|4: Deploy Archive | [3-deploy_web_static.py](https://github.com/Oliveth96/AirBnB_clone_v2/blob/dev/3-deploy_web_static.py) | Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy |

|5: Delete out-of-date archives | [100-clean_web_static.py](https://github.com/Oliveth96/AirBnB_clone_v2/blob/dev/100-clean_web_static.py) |A  Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives, using the function do_clean |


|6: prepare your web browsers | [101-setup_web_static.pp] (https://github.com/Oliveth96/AirBnB_clone_v2/blob/dev101-setup_web_static.pp) | A Bash script that sets up your web servers for the deployment of web_static |

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

