# AirBnB_clone

![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/98347450/176753474-73587c02-91d9-4065-8dbf-a98c12a319df.png)

## Concept

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

* A website (the front-end) that shows the final product to everybody: static and dynamic

* A database or files that store data (data = objects)

* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## First step: Write a command interpreter to manage your AirBnB objects. This is the first step towards building your first full web application: the AirBnB clone.

***This first step is very important because you will use what you build during this project with all other following projects.***

* Implement the parent class called "BaseModel"

* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

* Create the first abstracted storage engine of the project: File storage.

* Create all unittests to validate all our classes and storage engine

## What’s a command interpreter?

* Create a new object (ex: a new User or a new Place)

* Retrieve an object from a file, a database etc…

* Do operations on objects (count, compute stats, etc…)

* Update attributes of an object

* Destroy an object

## Resources

* Python abstract classes

* cmd module

* Packages concept page

* uuid module

* datetime

* unittest module

* args/kwargs

* Python test cheatsheet

## General

* How to create a Python package ?

* First, we create a directory and give it a package name, preferably related to its operation. Then we put the classes and the required functions in it. Finally we create an __init__.py file inside the directory, to let Python know that the directory is a package.
* How to create a command interpreter in Python using the cmd module ?

* What is Unit testing and how to implement it in a large project ?

* How to serialize and deserialize a Class ?

* How to write and read a JSON file ?

* How to manage datetime ?

* What is an UUID ?

* What is *args and how to use it ?

* What is **kwargs and how to use it ?

* How to handle named arguments in a function ?

## Requirements

* Python Scripts

* Allowed editors: vi, vim, emacs

* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

* All your files should end with a new line

* The first line of all your files should be exactly #!/usr/bin/python3

* A README.md file, at the root of the folder of the project, is mandatory

* Your code should use the pycodestyle (version 2.8.*)

* All your files must be executable

* The length of your files will be tested using wc

* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')

* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Python Unit Tests

* Allowed editors: vi, vim, emacs

* All your files should end with a new line

* All your test files should be inside a folder tests

* You have to use the unittest module

* All your test files should be python files (extension: .py)

* All your test files and folders should start by test_

* Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py

* All your tests should be executed by using this command: python3 -m unittest discover tests

* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py

* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')

* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Execution

Your shell should work like this in interactive mode:

```

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

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
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```

*All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash*

## The Console (step 1)

![815046647d23428a14ca](https://user-images.githubusercontent.com/98347450/176764791-0edd30cc-fc6a-4523-a737-318b583ae669.png)

## Console: Command interpreter

*Prompt* : (hbnb)

| Command | Description |
-----------------------
| quit | To exit the console |
| EOF | To exit the console by EOF |
| Empty Line + ENTER | ..... |
| help | Display the help documention |

