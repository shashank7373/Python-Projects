This is simple membership tracking application

There are 3 main types functions to run this app
  1. A program to get the output directly on the command line. (main.py)
  2. A program to test all the test cases using pytest module. (test_pytest_renewal_rem.py)
  3. A program to display all the test cases along with their respective outputs in a tkinter app. (basic_app_design.py)

All these programs can be run using the basic "python" or "python -m pytest" commands

There are 2 test files with different test cases for different membership renewal dates. (The file names are self explanatory)

The default setting in the program runs test cases for "15-03-2020" renewal date. You can change this by changing the renewstr to
"15-01-2020" in all the 3 programs mentioned above. If you want to run test cases for the changed renewal date you do so by changing the file name inside the "test_pytest_renewal_rem.py" and "basic_app_design.py" files. (Where to change is written in comments inside the files)
