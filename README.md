# Credit_Calculator_Test_Automation
The Script is designed to verify if data provided by Credit Calculator are correct.

It uses 2 Python Scripts and 1 Excel file:

1)  Credit_Calculator_Test_Cases.xlsx - Excel file - contains Test Cases with data that are to be provided to the app and information on the results of the tests
2)  Credit_Calculator_Calculator.py - Python file - takes data provided in Test Cases, provides them into the App using webdriver, validates correctness of result given by the App with expected result given in Test Cases
3)  Excel_Utils.py - Python file - contains set of functions that deal with operating Excel files using "openpyxl"
