The Python tutorial
doctest — Test interactive Python examples until 26.2.3.7. Warnings included and doctest – Testing through documentation.
Learn to Program.
A simple introduction to Object Oriented Programming without going into much detail:
Read everything until the paragraph “Inheritance” excluded
You do NOT have to learn about class attributes, classmethod and staticmethod yet
Object-Oriented Programming. Please be careful: in most of the following paragraphs, the author shows things the way you should not use or write a class, in order to make you better understand some concepts and how everything works in Python 3. Make sure you read everything. Read only the following paragraphs:
General Introduction
First-class Everything
A Minimal Class in Python
Attributes
You NOT have to learn about class attributes
Methods
The __init__ Method
Data Abstraction, Data Encapsulation, and Information Hiding
Public- Protected- and Private Attributes
Properties vs. Getters and Setters
TL;DR; - A good wrap-up video about everything you need to know for this project: Learn to Program 9 : Object Oriented Programming
TL;DR;

install it: sudo apt-get install python3-pep8 (version 1.7)
alternative install using pip3 (Python3 version of pip): Install
If /usr/bin/pep8 doesn’t exist, pep8 is located here /usr/local/lib/python3.4/dist-packages/pep8.py or /usr/lib/python3.4/dist-packages/pep8.py (cp /usr/local/lib/python3.4/dist-packages/pep8.py /usr/bin/pep8 && chmod u+x /usr/bin/pep8 or cp /usr/lib/python3.4/dist-packages/pep8.py /usr/bin/pep8 && chmod u+x /usr/bin/pep8)
use it: pep8 file.py
… and of course, last but not least: man python3

What you should learn from this project
At the end of this project you are expected to be able to explain to anyone, without the help of Google:

Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
Who created Python
Who is Guido van Rossum
Where does the name ‘Python’ come from
How to use the Python interpreter
All basics of Python syntax
What is the official Holberton Python coding style and how to check your code with PEP 8
Requirements for Python scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
All your imported files must be in the alphabetic order
Requirements for Python test cases
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
example: guillaume@ubuntu:~/0x06$ python3 -m doctest -v ./tests/0-add_integer.txt
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge case
