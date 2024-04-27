# AirBnB Clone - The Console
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://media.designrush.com/inspiration_images/135187/conversions/_1511452487_364_Airbnb-desktop.jpg)

# Welcome to the AirBnB clone project!

## General:
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
Each task is linked and will help you to:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## What’s a command interpreter?
we want to be able to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
```
## how to use it:
First you run `./console.py` in you'r terminal, then write a command.

***create***: Creates a new instance.
Syntax => `create <class_name>`. Ex:
```
(hbnb) create BaseModel
03b0ac5f-bcf3-4ace-a643-9cbe794d45b1
```

***show***: Prints the string representation of an instance based on the class name and id.
Syntax => `show <class_name> <instance_id>`. Ex:
```
(hbnb) create BaseModel
03b0ac5f-bcf3-4ace-a643-9cbe794d45b1
(hbnb) show BaseModel 03b0ac5f-bcf3-4ace-a643-9cbe794d45b1
[BaseModel] (6595e783-da15-4f39-82ed-b61ab8db97c8) {'id': '6595e783-da15-4f39-82ed-b61ab8db97c8', 'created_at': datetime.datetime(2024, 2, 10, 5, 17, 36, 967334), 'updated_at': datetime.datetime(2024, 2, 10, 5, 17, 36, 967346)}
```

***destroy***: Deletes an instance based on the class name and id.
Syntax => `destroy <class_name> <instance_id>`. Ex:
```
(hbnb) create BaseModel
03b0ac5f-bcf3-4ace-a643-9cbe794d45b1
(hbnb) show BaseModel 03b0ac5f-bcf3-4ace-a643-9cbe794d45b1
[BaseModel] (6595e783-da15-4f39-82ed-b61ab8db97c8) {'id': '6595e783-da15-4f39-82ed-b61ab8db97c8', 'created_at': datetime.datetime(2024, 2, 10, 5, 17, 36, 967334), 'updated_at': datetime.datetime(2024, 2, 10, 5, 17, 36, 967346)}
(hbnb)
(hbnb) destroy BaseModel 03b0ac5f-bcf3-4ace-a643-9cbe794d45b1
(hbnb) show BaseModel 03b0ac5f-bcf3-4ace-a643-9cbe794d45b1
** no instance found **
(hbnb)
```

***all***: Prints all string representation of all instances based or not on the class name.
Syntax => `all <class_name>`. Ex:
```
(hbnb) create BaseModel
e7c811b1-1f11-4952-95e4-e378b7c59512
(hbnb) create BaseModel
03b0ac5f-bcf3-4ace-a643-9cbe794d45b1
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (e7c811b1-1f11-4952-95e4-e378b7c59512) {'id': 'e7c811b1-1f11-4952-95e4-e378b7c59512', 'created_at': datetime.datetime(2024, 2, 9, 22, 21, 16, 248569), 'updated_at': datetime.datetime(2024, 2, 9, 22, 53, 46, 180385)}", "[BaseModel] (03b0ac5f-bcf3-4ace-a643-9cbe794d45b1) {'id': '03b0ac5f-bcf3-4ace-a643-9cbe794d45b1', 'created_at': datetime.datetime(2024, 2, 10, 5, 12, 59, 16448), 'updated_at': datetime.datetime(2024, 2, 10, 5, 12, 59, 16475)}"]
(hbnb)
```

***update***: Updates an instance based on the class name and id by adding or updating attribute.
Syntax => `update <class name> <id> <attribute name> "<attribute value>"`. Ex:
```
(hbnb) create BaseModel
e7c811b1-1f11-4952-95e4-e378b7c59512
(hbnb) create BaseModel
03b0ac5f-bcf3-4ace-a643-9cbe794d45b1
(hbnb)
(hbnb) show BaseModel e7c811b1-1f11-4952-95e4-e378b7c59512
[BaseModel] (e4a2ed29-de95-460e-a569-f15b911163b6) {'id': 'e4a2ed29-de95-460e-a569-f15b911163b6', 'created_at': datetime.datetime(2024, 2, 10, 5, 31, 17, 80460), 'updated_at': datetime.datetime(2024, 2, 10, 5, 31, 17, 80469)}
(hbnb)
(hbnb) update BaseModel e7c811b1-1f11-4952-95e4-e378b7c59512 first_name "Betty"
(hbnb) show BaseModel e7c811b1-1f11-4952-95e4-e378b7c59512
[BaseModel] (e4a2ed29-de95-460e-a569-f15b911163b6) {'first_name': 'Betty', 'id': 'e4a2ed29-de95-460e-a569-f15b911163b6', 'created_at': datetime.datetime(2024, 2, 10, 5, 31, 17, 80460), 'updated_at': datetime.datetime(2024, 2, 10, 5, 31, 17, 80469)}
(hbnb)
```

# Finally
If you want more info you're simply write `help` or `help <command>`. to exit the program, write `EOF` or `quit`:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help all

        Prints all string representation of all instances
        based or not on the class name.
        Usage: all OR all <class name>
(hbnb)
(hbnb) EOF
root@DESKTOP-V3KONQG:~/alx/AirBnB_clone$
```
