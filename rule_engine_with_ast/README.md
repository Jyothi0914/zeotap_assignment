Rule Engine with AST

Project Overview
This project implements a Rule Engine using an Abstract Syntax Tree (AST) to evaluate dynamic rules based on user attributes like age, department, income, and experience. The system supports the creation, combination, and evaluation of rules through a RESTful API built using Flask. The rules are stored in a PostgreSQL database, and the engine evaluates user data against these rules to determine eligibility.

Features
-> AST Representation: Dynamically parse rule strings into an Abstract Syntax Tree.
-> Rule Combination: Combine multiple rules using logical operators (AND/OR).
-> Rule Evaluation: Evaluate rules against user data in JSON format.
-> API Endpoints: Flask-based REST API for rule creation, combination, and evaluation.
-> Logging and Error Handling: Robust error handling and logging to track issues.

Prerequisites
Before running the project, ensure you have the following installed:
1. Python 3.9 or higher: Download and install from Python official website.
2. PostgreSQL: Set up a PostgreSQL instance for storing rules.
3. Git: To upload the project to GitHub.

Python Dependencies
-> Flask (for the REST API)
-> psycopg2-binary (for PostgreSQL interaction)
-> python-dotenv (for environment variable management)

Project Setup
1. Clone the repository (after uploading to GitHub)
	git clone <your-repository-url>
	cd rule_engine_with_ast

2. Create and activate a Python virtual environment
	# On Windows
	python -m venv venv
	venv\Scripts\activate

3. Install dependencies
	pip install -r requirements.txt

4. Configure PostgreSQL Database
Ensure PostgreSQL is running on your machine and create a database for the project:
	CREATE DATABASE rule_engine;
	CREATE USER your_username WITH PASSWORD 'your_password';
	GRANT ALL PRIVILEGES ON DATABASE rule_engine TO your_username;

5. Set up environment variables
Create a .env file in the root directory and add your PostgreSQL connection details:
	DB_HOST=localhost
	DB_NAME=rule_engine
	DB_USER=your_username
	DB_PASSWORD=your_password

6. Create the Database Schema
Run the following SQL script to create the rules table in PostgreSQL:
	CREATE TABLE rules (
    		id SERIAL PRIMARY KEY,
    		rule_string TEXT NOT NULL,
    		ast TEXT NOT NULL
	);

7. Running the Application
To start the Flask server, run:
	python app.py
The API will be available at http://localhost:5000.

8. API Endpoints
1. Create a Rule
-> URL: /create_rule
-> Method: POST
-> Description: Accepts a rule string and creates the corresponding AST.
-> Request Body:
	json
	{
    		"rule_string": "(age > 30 AND department == 'Sales')"
	}
-> Response:
	{
    		"ast": "<AST representation>"
	}

2. Combine Rules
-> URL: /combine_rules
-> Method: POST
-> Description: Combines multiple rules into a single AST.
-> Request Body:
{
    "rules": [
        "(age > 30 AND department == 'Sales')",
        "(salary > 50000)"
    ],
    "operator": "AND"
}
-> Response:
{
    "combined_ast": "<Combined AST representation>"
}

3. Evaluate a Rule
-> URL: /evaluate
-> Method: POST
-> Description: Evaluates a rule against user data.
-> Request Body:
{
    "rule_id": 1,
    "data": {
        "age": 35,
        "department": "Sales",
        "salary": 60000
    }
}
-> Response:
{
    "result": true
}

9. Testing
You can use Postman or cURL to test the API endpoints.
Unit tests are provided in the tests/ folder. Run the tests using:
	python -m unittest discover tests

10. Logging and Error Handling
The project includes logging to track API requests and errors.
Errors are handled gracefully and returned as JSON responses.