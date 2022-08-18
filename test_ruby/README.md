## CREATION GOAL
This project is a test assignment for a trainee Ruby developer position. My personal goal was to develop a console application that would execute the necessary functionality under any correct or incorrect user commands using OOP.

## NOTABLE MOMENTS
All commands listed in this README file may vary according to your system settings.
The most common difference may be in Python calling with console commands, as it can be done with keyword 'python' or 'python3' or 'py' and so on.


## REQUIREMENTS
The current version of the product requires Python 3.10. The product has not been tested on earlier versions of the Python interpreter.
This console application does not require any third-party packages other than coverage to see the percentage of test coverage. It works with the built-in SQLite3 library.
You need to install python on your machine for the product to work. 
- On Windows it is easily done by installation of a setup file downloaded from  http://www.python.org. 
- A quick guide for updating it on Ubuntu can be found here:
https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/
```
coverage==6.4.4
```
## INSTALLATION
```
1. Copy or extract root directory of app (test_ruby) with all files and subdirectories to a local directory.

2. Install and activate virtual environment, to do it, use following commands while being in root directory of the app:

    2.1. $ python -m venv venv (for UNIX-based systems) 
         or 	
         python -m venv venv (for Windows)

    2.2. $ source venv/bin/activate  (for UNIX-based systems) 
         or
         venv\Scripts\activate.bat or venv\Scripts\activate.ps1 or venv\Scripts\activate (for Windows)

3. Install required packages(coverage) to your fresh virtual environment, to do it use following command while being in root directory 
of the app:

    3.1. $ pip install -r requirements.txt (for UNIX-based systems) 
         or 	
         pip install -r requirements.txt (for Windows)
```

## USING CONSOLE APP
To get started with the console application you can:    

1. Run the application with the console command  'python main.py' as a script from the root directory(test_ruby) of the application.

2. Launch the application using any IDE you like(PyCharm, VsCode, vim etc.)

The application works with two databases - a SQLite database(cost-control.db) and a text database (users.txt).
After starting, the application asks for a login. If the entered username exists in users.txt, the application displays the message 'Welcome back, {user}', 
If there is no match, the application registers a new user and enters the login into the text database. 
A message appears on the screen saying that the new user is registered. 
A database is created that has columns (User, Date, Category, Expense ). If the user selects the "add" command, today's date is written to the database as the default.

After user identification, the following commands are available:
add, get stat, clear, d/m/y, awd

Absolutely all command entries are converted to lower case and remove unnecessary spaces on the left and right to read the statistics correctly when needed.
All manipulations with databases except the user identification function are done with SQL queries (CREATE TABLE, INSERT, SELECT, DELETE etc.)
If the user enters an unknown command at any point in the program, the application uses recursion to re-run the function where that command was entered until the user's input is valid.


```
Command 'add' - The command that adds an expense by category. The 'Category' field cannot be empty and cannot be a number. 
          If the user leaves it blank or input number, the application will ask to enter the category again until it is filled right.  
          The "Expense" field must be either an integer or a natural number. If the user enters a string, the application displays a message 
          that the entry is invalid and asks to enter the category and expense again. 
          If the user enters a negative number, the minus is discarded and the same number with a positive sign is entered into the database. 
          After adding an expense to the database, the application thanks the user and tells which category and which expense was entered in the database.



The "get stat" command -  outputs statistics either for a given category, if the user entered a specific one, or all statistics, if the user entered "all". 
          If the user wanted to see all statistics, it will display the flow for each category and at the end of the summary, total. 
          If the category for which the query was made does not exist, the expense for that category will be displayed, which will be 0.



Command "clear" - Deletes all data from two databases (cost-control.db and users.txt). At the end it displays a message that all data has been deleted.



The 'd/m/y' command - allows the user to select the day, month or year for which the user wants to get expense statistics. After entering the command, 
          the application asks for either 'day', 'month' or 'year'. After selecting one of the three, the application asks for the date in a specific format (YYYYY-MM-DD).
          If the date entered is not valid, the app displays a message and asks to do so again until a valid date is entered. 
          If the user has selected "month" or "year", the application asks for the day of the count from which to start, if "day", the statistics for that day are displayed. 



The "awd" command allows the user to add an expense by date. The validity of the date is checked in the same way as in the d/m/y command, 
          and the validity of the expense and category entry is checked in the same way as in the "add expense" command. 
```
## BASIC FUNCTIONALITY
All the functionality of the application is written in the functionality.py module. 
the Functionality class is the base class for manipulating the database, checking the validity of input commands, the validity of date, the validity of cost input.

## TESTING
Unittests for the app are located in app directory, which is by default the 'test_ruby' directory  in file tests.py.
To run unittests for the app user can use following command while being in app directory:
```
$ python -m unittest tests.py (for UNIX-based systems) 
or
python -m unittest tests.py (for Windows)
```
Test coverage for current version is:
```
Name               Stmts   Miss  Cover
--------------------------------------
functionality.py     155     50    68%
tests.py              94      0   100%
--------------------------------------
TOTAL                249     50    80%

```




