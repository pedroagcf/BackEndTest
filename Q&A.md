### :speaking_head: Instructions

<img src="https://raw.githubusercontent.com/MicaelliMedeiros/micaellimedeiros/master/image/computer-illustration.png" min-width="400px" max-width="400px" width="400px" align="right" alt="TomDatalab">

<p align="left"> 
  Choose a quiet and peaceful place to perform the tests. The main objective is that we can understand the level of knowledge of the candidate. Be honest with your answers. There is no pre-established time for completing the tests, <strong>do your best</strong>.<br>
</p>

## <img width="45" alt="about" src="https://raw.github.com/elizarov/elizarov/master/about.png"> Good luck !

# :speaking_head: Part I - Python

:blue_book: <strong><b>1)</b></strong> What is Python? What are the benefits of using Python

- Python it's a modern programming language that is helpful in several contexts, such as web development, artificial intelligence, data science, embedded devices

:blue_book: <strong><b>2)</b></strong> What is a dynamically typed language?

- It means that the variable type will be assigned in runtime. Also, the same variable can assume different types during the execution.

:blue_book: <strong><b>3)</b></strong> What is an Interpreted language?

- It's about the approach used to run the code instructions. So, in that case, there is no compiling step.

:blue_book: <strong><b>4)</b></strong> What is PEP 8 and why is it important?

- PEP 8 is a python guideline and it's important because promote standarts and best practices into the project.

:blue_book: <strong><b>5)</b></strong> What is Scope in Python?

- the scope represent where the variable can be accessed.

:blue_book: <strong><b>6)</b></strong> What are lists and tuples? What is the key difference between the two?

- lists and tuples are data structures utilized to store objects, numbers, strings, etc..

:blue_book: <strong><b>7)</b></strong> What are the common built-in data types in Python?

- boolean, string, int, float, list, dict,

:blue_book: <strong><b>8)</b></strong> What is pass in Python?

- n/a

:blue_book: <strong><b>9)</b></strong> What are modules and packages in Python?

- It's about how the code is separated and organized. So, you could have one package composed by a lot of modules.

:blue_book: <strong><b>10)</b></strong> What are global, protected and private attributes in Python?

- These concepts are related with encapsulation in OOP. So, private attributes are accessible only inside of the class. protected attributes are accessible only in the classes and inherited classes. In the end, public are accessible out of the class.

:blue_book: <strong><b>11)</b></strong> What is the use of self in Python?

- self is a reserved name to refer of the context or scope. For instance, with 'self' we can refer the classes attributes.

:blue_book: <strong><b>12)</b></strong> What is **init**?

- class constructor.

:blue_book: <strong><b>13)</b></strong> What is break, continue and pass in Python?

- break and continue are commonly utilized inside loops + conditional structures.
- break: just interrupt the execution.
- continue: skip the current index inside loop.

:blue_book: <strong><b>14)</b></strong> What are unit tests in Python?

- unit tests are a approach to test each individual part of an application.

:blue_book: <strong><b>15)</b></strong> What is docstring in Python?

- docstring is used to create good documentations.

:blue_book: <strong><b>16)</b></strong> What is slicing in Python?

- method that allow to select a piece of string or array.

:blue_book: <strong><b>17)</b></strong> Explain how can you make a Python Script executable on Unix?

- n/a

:blue_book: <strong><b>18)</b></strong> What is the difference between Python Arrays and lists?

- n/a

:blue_book: <strong><b>19)</b></strong> How is memory managed in Python?

- n/a

:blue_book: <strong><b>20)</b></strong> What are Python namespaces? Why are they used?

- n/a

:blue_book: <strong><b>21)</b></strong> What is Scope Resolution in Python?

-n/a

:blue_book: <strong><b>22)</b></strong> What are decorators in Python?

- design pattern that add/change extra functionality to an existent function/object.

:blue_book: <strong><b>23)</b></strong> What are Dict and List comprehensions?

- It's a shorthand to iterate over a list or dict and perform some extra logic returning a new data structure.

:blue_book: <strong><b>24)</b></strong> What is lambda in Python? Why is it used?

- lambda in python is an anonymous function declared inline. This approach promotes functional programming and better maintenance.

:blue_book: <strong><b>25)</b></strong> How do you copy an object in Python?

- n/a

:blue_book: <strong><b>26)</b></strong> What is the difference between xrange and range in Python?

- n/a

:blue_book: <strong><b>27)</b></strong> What is pickling and unpickling?

- n/a

:blue_book: <strong><b>28)</b></strong> What are generators in Python?

- A generator function return iterators giving more control over the iterations.

:blue_book: <strong><b>29)</b></strong> What is PYTHONPATH in Python?

- n/a

:blue_book: <strong><b>30)</b></strong> What is the use of help() and dir() functions?

- help: function thar returns support information about python data structures.
- dir: function that returns more details about an object

:blue_book: <strong><b>31)</b></strong> What is the difference between .py and .pyc files?

- n/a

:blue_book: <strong><b>32)</b></strong> How Python is interpreted?

- n/a

:blue_book: <strong><b>33)</b></strong> How are arguments passed by value or by reference in python?

- n/a

:blue_book: <strong><b>34)</b></strong> What are iterators in Python?

- It's an object that iterate over list, array, etc..

:blue_book: <strong><b>35)</b></strong> Explain how to delete a file in Python?

- n/a

:blue_book: <strong><b>36)</b></strong> Explain split() and join() functions in Python?

- split: takes an string and return and array divided by argument in the split function. "test".split() => ["t", "e", "s", "t"]
  -join: Similar join method will takes an array and return a new string. ["t", "e", "s", "t"].join(",") => "test"

:blue_book: <strong><b>37)</b></strong> What does \*args and \*\*kwargs mean?

- n/a

:blue_book: <strong><b>38)</b></strong> What are negative indexes and why are they used?

- With negative indexes we can access arrays, lists, strings by the end.

:blue_book: <strong><b>39)</b></strong> How do you create a class in Python?

- Doing this:
  "  
   class Foo:
  ...
  "

:blue_book: <strong><b>40)</b></strong> How does inheritance work in python? Explain it with an example.

"
class Human:
def walk():
...

class Men(Human):
def run():
...

m = Men()

m.walk()
m.run()
"

:blue_book: <strong><b>41)</b></strong> How do you access parent members in the child class?

- with super method.

:blue_book: <strong><b>42)</b></strong> Are access specifiers used in python?

- no

:blue_book: <strong><b>43)</b></strong> Is it possible to call parent class without its instance creation?

- Yes

:blue_book: <strong><b>44)</b></strong> How is an empty class created in python?

- n/a

:blue_book: <strong><b>45)</b></strong> Differentiate between new and override modifiers.

- n/a

:blue_book: <strong><b>46)</b></strong> Why is finalize used?

- n/a

:blue_book: <strong><b>47)</b></strong> What is init method in python?

- init method represent the class constructor

:blue_book: <strong><b>48)</b></strong> How will you check if a class is a child of another class?

- n/a

:blue_book: <strong><b>49)</b></strong> What do you know about pandas?

- pandas is a very powerful library that allow us to read, write and manipulate datasets. Is very used in the data science context.

:blue_book: <strong><b>50)</b></strong> Define pandas dataframe.

- It's a data structure used to manipulate data.

:blue_book: <strong><b>51)</b></strong> How will you combine different pandas dataframes?

using pd.concat method

:blue_book: <strong><b>52)</b></strong> Can you create a series from the dictionary object in pandas?

- yes.

:blue_book: <strong><b>53)</b></strong> How will you identify and deal with missing values in a dataframe?

- dropping the columns or setting null

:blue_book: <strong><b>54)</b></strong> What do you understand by reindexing in pandas?

- It's like to rearrange the dataframe

:blue_book: <strong><b>55)</b></strong> How to add new column to pandas dataframe?

- n/a

:blue_book: <strong><b>56)</b></strong> How will you delete indices, rows and columns from a dataframe?

- n/a

:blue_book: <strong><b>57)</b></strong> Can you get items of series A that are not available in another series B?

- yes

:blue_book: <strong><b>58)</b></strong> How will you get the items that are not common to both the given series A and B?

- n/a

:blue_book: <strong><b>59)</b></strong> While importing data from different sources, can the pandas library recognize dates?

- n/a

:blue_book: <strong><b>60)</b></strong> What do you understand by NumPy?

- NumPy is a lib to handle with math operations.

:blue_book: <strong><b>61)</b></strong> How are NumPy arrays advantageous over python lists?

- n/a

:blue_book: <strong><b>62)</b></strong> What are the steps to create 1D, 2D and 3D arrays?

- n/a

:blue_book: <strong><b>63)</b></strong> You are given a numpy array and a new column as inputs. How will you delete the second column and replace the column with a new column value?

- n/a

:blue_book: <strong><b>64)</b></strong> How will you efficiently load data from a text file?

- n/a

:blue_book: <strong><b>65)</b></strong> How will you read CSV data into an array in NumPy?

- n/a

:blue_book: <strong><b>66)</b></strong> How will you sort the array based on the Nth column?

- n/a

:blue_book: <strong><b>67)</b></strong> How will you find the nearest value in a given numpy array?

- n/a

:blue_book: <strong><b>68)</b></strong> How will you reverse the numpy array using one line of code?

- n/a

:blue_book: <strong><b>69)</b></strong> How will you find the shape of any given NumPy array?

- n/a

:blue_book: <strong><b>70)</b></strong> Differentiate between a package and a module in python.

- A package can be composed by different modules.

:blue_book: <strong><b>71)</b></strong> What are some of the most commonly used built-in modules in Python?

- os, path, math, time

:blue_book: <strong><b>72)</b></strong> What are lambda functions?

- lambda in python is an anonymous function declared inline. This approach promotes functional programming and better maintenance.

:blue_book: <strong><b>73)</b></strong> How can you generate random numbers?

- math.random()

:blue_book: <strong><b>74)</b></strong> Can you easily check if all characters in the given string is alphanumeric?

:blue_book: <strong><b>75)</b></strong> What are the differences between pickling and unpickling?

- n/a

:blue_book: <strong><b>76)</b></strong> Define GIL.

- n/a

:blue_book: <strong><b>77)</b></strong> Define PYTHONPATH.

- environment variable

:blue_book: <strong><b>78)</b></strong> Define PIP.

- It's a package manager

:blue_book: <strong><b>79)</b></strong> Are there any tools for identifying bugs and performing static analysis in python?

- yes, such as: Sonarqube, pyCharm, codacy, embold.

:blue_book: <strong><b>80)</b></strong> Differentiate between deep and shallow copies.

- n/a

:blue_book: <strong><b>81)</b></strong> What is main function in python? How do you invoke it?

- It's used to execute when the script run.

:blue_book: <strong><b>82)</b></strong> Write python function which takes a variable number of arguments.

"
def foo(\*args):
for arg in args:
print(arg)

foo(1, 2, 3,)
"

:blue_book: <strong><b>83)</b></strong> WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.

:blue_book: <strong><b>84)</b></strong> Write a program for counting the number of every character of a given text file.

:blue_book: <strong><b>85)</b></strong> Write a program to check and return the pairs of a given array A whose sum value is equal to a target value N.

:blue_book: <strong><b>86)</b></strong> Write a Program to add two integers >0 without using the plus operator.

:blue_book: <strong><b>87)</b></strong> Write a Program to solve the given equation assuming that a,b,c,m,n,o are constants:

:blue_book: <strong><b>88)</b></strong> Write a Program to match a string that has the letter ‘a’ followed by 4 to 8 'b’s.

:blue_book: <strong><b>89)</b></strong> Write a Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.

:blue_book: <strong><b>90)</b></strong> Write a Program to combine two different dictionaries. While combining, if you find the same keys, you can add the values of these same keys. Output the new dictionary

:blue_book: <strong><b>91)</b></strong> How will you access the dataset of a publicly shared spreadsheet in CSV format stored in Google Drive?

# :speaking_head: Part II - Django

:blue_book: <strong><b>1)</b></strong> Explain Django Architecture?

- n/a

:blue_book: <strong><b>2)</b></strong> Explain the django project directory structure?

- n/a

:blue_book: <strong><b>3)</b></strong> What are models in Django?

- Models in django are entities representation into the database.

:blue_book: <strong><b>4)</b></strong> What are templates in Django or Django template language?

- n/a

:blue_book: <strong><b>5)</b></strong> What are views in Django?

- n/a

:blue_book: <strong><b>6)</b></strong> What is Django ORM?

- Object Relational Mapping: is a interface to interact with the database.

:blue_book: <strong><b>7)</b></strong> Define static files and explain their uses?

- n/a
  :blue_book: <strong><b>8)</b></strong> What is Django Rest Framework(DRF)?

It's a tool to build backend applications.

:blue_book: <strong><b>9)</b></strong> What is django-admin and manage.py and explain its commands?

- n/a

:blue_book: <strong><b>10)</b></strong> What is Jinja templating?

- n/a

:blue_book: <strong><b>11)</b></strong> What are Django URLs?

- route definitions

:blue_book: <strong><b>12)</b></strong> What is the difference between a project and an app in Django?

- n/a

:blue_book: <strong><b>13)</b></strong> What are different model inheritance styles in the Django?

- n/a

:blue_book: <strong><b>14)</b></strong> What are Django Signals?

- n/a

:blue_book: <strong><b>15)</b></strong> Explain the caching strategies in the Django?

- n/a

:blue_book: <strong><b>16)</b></strong> Explain user authentication in Django?

- n/a

:blue_book: <strong><b>17)</b></strong> How to configure static files?

- n/a

:blue_book: <strong><b>18)</b></strong> Explain Django Response lifecycle?

- n/a

:blue_book: <strong><b>19)</b></strong> What databases are supported by Django?

- n/a

:blue_book: <strong><b>20)</b></strong> What's the use of a session framework?

- n/a

:blue_book: <strong><b>21)</b></strong> What’s the use of Middleware in Django?

- n/a

:blue_book: <strong><b>22)</b></strong> What is context in the Django?

-n/a

:blue_book: <strong><b>23)</b></strong> What is django.shortcuts.render function?

-n/a

:blue_book: <strong><b>24)</b></strong> What’s the significance of the settings.py file?

- -n/a

:blue_book: <strong><b>25)</b></strong> How to view all items in the Model?

-n/a

:blue_book: <strong><b>26)</b></strong> How to filter items in the Model?

- like this: Dividend.objects.filter(symbol=symbol, date=date, amount=amount)

:blue_book: <strong><b>27)</b></strong> How to use file-based sessions?

- n/a

:blue_book: <strong><b>28)</b></strong> What is mixin?

- n/a

:blue_book: <strong><b>29)</b></strong> What is Django Field Class?

- n/a

:blue_book: <strong><b>30)</b></strong> Why is permanent redirection not a good option?

- n/a

:blue_book: <strong><b>31)</b></strong> Difference between Django OneToOneField and ForeignKey Field?

- n/a

:blue_book: <strong><b>32)</b></strong> How can you combine multiple QuerySets in a View?

- n/a

:blue_book: <strong><b>33)</b></strong> How to get a particular item in the Model?

- n/a

:blue_book: <strong><b>34)</b></strong> How to obtain the SQL query from the queryset?

- n/a

:blue_book: <strong><b>35)</b></strong> What are the ways to customize the functionality of the Django admin interface?

- n/a

:blue_book: <strong><b>36)</b></strong> Difference between select_related and prefetch_related?

- n/a

:blue_book: <strong><b>37)</b></strong> Explain Q objects in Django ORM?

- n/a

:blue_book: <strong><b>38)</b></strong> What are Django exceptions?

- n/a
