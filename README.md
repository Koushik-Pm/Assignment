Project Structure Overview
------
Credentials - I have created a JSON file to store my username and password
------
page_object_model  - I have created 2 test for login and form filling page
------
tests - to run test cases
------
webdriver_setup - To install Chrome driver
------

Step 1 - Clone the repository
------
Step 2 - Install the required libraries 
pip install -r requirements.txt
------
Step 3 - To run all the test execute the below command 
pytest or python -m pytest
------
Step 4 - To run test cases individually 
Login page - pytest tests/test_login.py
Form Submission page - pytest tests/test_form.py
------
Test Cases
Login Test– Tests login using valid credentials.
Form Submission Test – Fills checkout form using Faker data.
------
Step 5 - To generate HTML report, execute the below command 
pytest --html=reports/test_report.html
------

The Login page uses credentials from JSON file and verifies successful login by checking the presence of a dashboard element
------
The Form filling page uses Faker library to generate Fake fields and it verifies successful checkout by presence of a text message
------
Used Explicit wait everywhere instead of static sleeps
------
The test cases were written using pytest and POM was implemented
------
