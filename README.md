# Python 3x Learning - ATB 
https://sdet.live/python0x

Below are the key topics to learn in Python, organized as bullet points for easy reference:

- **Python Basics**
  - Introduction to Python
  - Installation and Setup
  - Running Python Programs
  - Python Syntax
  - Variables and Data Types
  - Basic Operators
  - Control Flow
    - If Statements
    - Loops (For, While)

- **Functions**
  - Defining Functions
  - Function Arguments
  - Return Statement
  - Lambda Functions
  - Map, Filter, and Reduce Functions
  - Recursion

- **Strings**
  - String Manipulation
  - String Methods
  - Formatting Strings
  - Regular Expressions

- **Data Structures**
  - Lists
    - List Methods
    - List Comprehensions
  - Tuples
  - Dictionaries
    - Dictionary Methods
  - Sets
    - Set Methods

- **Modules and Packages**
  - Importing Modules
  - Standard Library Modules
  - Creating and Using Packages

- **File Handling**
  - Reading and Writing Files
  - Working with CSV and JSON Files

- **Error and Exception Handling**
  - Try, Except Blocks
  - Finally and Else Clauses
  - Custom Exceptions

- **Object-Oriented Programming (OOP)**
  - Classes and Objects
  - Inheritance
  - Polymorphism
  - Encapsulation
  - Method Overriding

- **Testing**
  - Test Automation with `pytest`


- **Web Development**
  - Introduction to Web Frameworks (Flask, Django)
  - Building Simple Web Applications

- **APIs**
  - Working with APIs
  - RESTful Services

- **Concurrency**
  - Multithreading
  - Multiprocessing
  - Asynchronous Programming (asyncio)

- **Version Control with Git**
  - Basic Git Commands
  - Branching and Merging
  - Collaborating with GitHub


### How to Work with the PyTest?
- pip install pytest
- File name - test_name.py
- Test name - test_name_of_test():
- Assert - Actual Result == Expected Result.

### How to run the PyTest?
- open cmd ->go the the folder - pytest
-  run icon

### PyTest Commands
- pytest -h
- To run all the testcases
  - pytest 
- To run specific testcase 
  - pytest ex02_July/22072024/test_Lab181.py
- To run specific testcase with pattern
  Ex: 
  pytest -k add	                | Chạy test có từ "add" trong tên
  pytest -k "add or sub"	      | Chạy test có từ "add" hoặc "sub"
  pytest -k "not multiply"	    | Bỏ qua test có từ "multiply"
  pytest -k "abc" test_file.py	| Lọc theo tên trong file cụ thể
- To run a specific marked Testcase 
  - Add a annotation @pytest.mark.regression
  - pytest -m "regression" ex02_July/22072024/test_Lab182.py
  - Ex: 
    Chạy test có marker smoke	          | pytest -m "smoke"
    Chạy test có marker regression	    | pytest -m "regression"
    Chạy test có cả hai marker	        | pytest -m "smoke and regression"
    Chạy test có smoke hoặc regression	| pytest -m "smoke or regression"
    Chạy test không có smoke	          | pytest -m "not smoke"
  - Remove warning
    Define marker in pytest.ini file in root folder
    [pytest]
    markers =
       smoke: marks smoke tests
       regression: marks regression tests

### How to see the Report of the PyTest Testcases?
- Make sure that allure commandline is installed
- Download the Node JS
- node -v
- npm install -g npm allure-commandline
- Install Java & set environement path
- Verify that allure -> options
- Run your Pytestcase - pytest ex02_July/22072024/test_Lab183.py --alluredir=allure_result
- allure serve allure_result

### How to Add Request Module to the Project
- pip install requests
- pytest ex02_July/24072024/test_Lab184.py --alluredir=allure_result
- -s -help you to print the details by print command

### API Automation Framework (Setup)
1. What is the Framework?
  - structure that provide a foundation for SW application/test automation
  - Key characteristics: 
    + provide structure for organizing code & resources.
    + profer folder structure to maintain the testcase
    + They follow best practices and design patterns
    + scalability & flexibility


2. Type of Framework in Automation Testing
  - Linear Automation Framework: 
    + Record & Playback: simple manner, much maintain, duplicate code
    + Ex: Find a API TC -> Create Booking - create_booking.py -> run it
  - Modular Driven Framework
    + divide TS into small module
    + easier maintainance, scability
    + eCom-API -> Registration -> Login -> Add to Cart -> Payment-> Order fullfilment-> Confirmation -> Shipping -> Refunds/Cancel
  - Data-Driven Testing Framework:
    + input single test script that execute test for all test data from a table and expect the test output in the same table
    + require programming, manage test data
  - Key-word driven Framework

  - <b><span style="color: red;">Behaviour Driven Developement: (BDD) Framework</b><span>
    + Given - When - Then
    + Human syntax
    + Eg: Cucumber
  - <b><span style="color: red;">Hybrid Testing Framework(Mixture of Modular, DDT, Keyword)</b><span>

3. Folder Structure of Framework

4. Running it via Jenkins + GIT (CI/CD)







