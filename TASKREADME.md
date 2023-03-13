# Backend Code Test

## The Test
Here at Test Company™ we’re interested in the daily exchange rate changes between various currencies and the US Dollar, which we will call `movements`.

Every morning between Monday to Friday we receive the rates from the previous `business day` in a CSV file and we manually compare the rates using the previous day’s data in a spreadsheet.

Our aim is to import the data into a database and then implement an API which will show the currency movements for a particular date. During the sprint planning we’ve highlighted the following tasks for the next sprint:

- Create a script that imports the fx rate data into a database
- Create an API Endpoint that shows the list of currency movements taking a date parameter

Non Functional Requirements
- Log any lines in the import files that contain invalid data
- Your API endpoint should use Flask
- Use a framework to create DB migrations for any models you create
- In the tests make sure at least one test checks erroneous lines are logged

## Info / Help

### Calculating Movements

The movements are currently calculated using the following calculation …

```python
movement = (1 - (current_date.exchange_rate / previous_date.exchange_rate)) * 100
```

### Expected API Output Format

(The actual values are only indicative)
```json
[
  {
    "currency_code": "JPY",
    "movement": 0.2301584257163758
  },
  {
    "currency_code": "KRW",
    "movement": -0.3666585186995919
  },
  /* ... etc */
]
```

## Submitting your work

Ideally send us a zip of your project, Github links are fine, but please don’t leave the repo publicly available after we have confirmed the receipt of your code.

Include all files you deem relevant such as migration files and requirements.

If there are any parts of the test that you struggle with, it's fine, just leave it till the end, focus on what you can do and we will judge the submission as a whole.

`Good luck!`
