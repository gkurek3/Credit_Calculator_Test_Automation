# Credit_Calculator_Test_Automation
The Script is designed to verify if data provided by Credit Calculator (www.totalmoney.pl) are correct.

It is based on Page Object Model and uses: Python, Selenium, Unit Test, Openpyxl

The idea is that the data for Test Cases are stored in an Excel File - "Credit_Calculator_Test_Cases.xlsx".
The Test script puts data from the Excel File into the Web Application and then, checks if the result of the 
monthly installment calculated by Web Application is correct. 
The script can also update the Excel File with the result (pass/fail) of the tests.
