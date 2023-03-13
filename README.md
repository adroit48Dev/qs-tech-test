# Task

- Create a script that imports the fx rate data into a database
- Create an API Endpoint that shows the list of currency movements taking a date parameter

## Sub-Task

### Non Functional Requirements
- Log any lines in the import files that contain invalid data
- Your API endpoint should use Flask
- Use a framework to create DB migrations for any models you create
- In the tests make sure at least one test checks erroneous lines are logged

### Assumption

- Create a database table to store the currency rates data
- Write a script to import the fx rate data from the CSV file into the database table
- Write an API endpoint using Flask to show the list of currency movements taking a date parameter
- Log any lines in the import files that contain invalid data
- Use a framework to create DB migrations for any models created
- Write tests to ensure that erroneous lines are logged


### Motive

- to avoid manual work and to store data in database with currency movements will help organization better workflow.

### personal notes
- approach TDD to finish this task
- try to create docker file
- log responses in separate file
- calculate currency movements

### folders & files structure (2 Levels)

├── app.py
├── config.py
├── currency.log
├── data
│   ├── fx_rates_1720230124.csv
│   ├── fx_rates_1720230125.csv
│   ├── fx_rates_1720230126.csv
│   ├── fx_rates_1720230127.csv
│   └── fx_rates_1720230130.csv
├── docker-compose.yml
├── Dockerfile
├── instance
│   ├── currency_data.db
│   └── currency.log
├── Pipfile
├── __pycache__
│   ├── app.cpython-39.pyc
│   └── config.cpython-39.pyc
├── README.md
├── requirements.txt
├── setup.cfg
├── src
│   ├── api
│   ├── __init__.py
│   ├── models.py
│   ├── __pycache__
│   └── status.py
├── TASKREADME.md
├── tests
│   ├── conftest.py
│   ├── fixtures
│   ├── __pycache__
│   ├── status.py
│   └── test_rates.py
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── man
    └── pyvenv.cfg

## Instructions to Run

- git clone this repo


- type 

`docker-compose up`

