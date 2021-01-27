# Dream Home API Back End Server
___
## About
This is the RESTful API back end server for [Dream Home](https://dream-home-cap.herokuapp.com/home). Dream Home walks users through an educative journey that ends in a analysis report that includes a timeline towards their projected home plan and future monthly payment details.

## Setup Instructions
- Production:
  - [Dream Home API](http://dreamhome-mvp.herokuapp.com)
  - Please see [Endpoint Documentation](#Endpoint-Documentation)
- Development:
  - Requirements:
    - `Python 3.9`
    - `Pip3`
    - `Pipenv`
    - `MongoDB`
  - Clone this repo
  - Enter virtual environment with `pipenv shell`
  - Install packages with `pip install -r requirements.txt`
  - Connect to database with `brew services start mongodb-community@<version>`
  - Create a `.env.dev` file at the root of the directory with the following code:
    ```
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost/dreamhome-dev'
    }
    ```
  - Run the server with: `python -m flask run`
  - This runs on `http://localhost:5000`
- Testing:
  - Create a `.env.test` file at the root of the directory with the following code:
    ```
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost/dreamhome-dev'
    }
    ```
  - To run all tests: `python -m unittest -b`
  - To run a single test: `python -m unittest tests/test_<file>.py`
  - To run coverage: `coverage run -m unittest discover`
  - To open coverage report: `open htmlcov/index.html` OR `coverage report -m` OR `coverage html`

## Tech stack
- [Python](https://www.python.org)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [MongoDB](https://www.mongodb.com)
- [MongoEngine](http://mongoengine.org)
- [Mongo Atlas](https://www.mongodb.com/cloud/atlas)
- [noSQL](https://en.wikipedia.org/wiki/NoSQL)
- [Heroku](https://www.heroku.com)
- [JSON](https://jsonapi.org)

## Team Contributions
- [Priya Power](https://github.com/priyapower): Backend Team Lead, Developer, Researcher, Backend Learning Coach
- [Arique Aguilar](https://github.com/Arique1104): Backend Developer, Deployment Guru, Frontend Liaison and Design Consultant
- [Eric Hale](https://github.com/EHale64): Backend Developer, Web Scraping Researcher, Error Pathing Standardization and Testing

## Endpoint Documentation
---
---
### Education
---
#### Call all education objects
  - Method/HTTP_Verb: GET
  - `/api/v1/education`
  - Body: NA
  - Returns:
    - All education objects nested under a custom key created from the objects `classification` field
    - Example response:
      ```json
      {
        "data": {
            "annual_salary": {
                "attributes": {
                    "classification": "Annual Salary",
                    "description": "Gross income is the total amount you earn (typically over the course of a year) before expenses. Net income is the profit your business earns after expenses ",
                    "information": "Depending on the home price you're aiming for, you may want to wait a year or two before you apply for a mortgage if you've just moved into a higher-paying role. The longer you stay in your higher-paying position, the more your lender may be willing to loan you.",
                    "note": "The amount of money you earn plays a smaller role in getting a mortgage than you might think. ",
                    "question": "What is your net monthly salary?",
                    "source": "https://www.rocketmortgage.com"
                },
                "id": "5fff12cfc4f364ae6e64eee5",
                "type": "Education object"
            },
            "credit_score": {
                "attributes": {
                    "classification": "Credit Score",
                    "description": " A high score will give you access to lower interest rates and more lender choices. If you have a low score, you may have trouble getting a loan.",
                    "information": "Your credit score plays a big role in the interest rate you'll get for your loan.",
                    "note": "Your credit score is a numerical rating that ranges from 300 – 850 and tells lenders how responsible you are when you borrow money. ",
                    "question": "What is your current credit score?",
                    "source": "https://www.rocketmortgage.com"
                },
                "id": "5fff1fd5f621c1b039b52d86",
                "type": "Education object"
            }
      }
      ```

#### Call a single education object by id
  - Method/HTTP_Verb: GET
  - `/api/v1/education/<id>`
  - Body: NA
  - Returns:
    - A single education object's information
    - Example response:
      ```json
      {
        "data": {
          "annual_salary": {
              "attributes": {
                  "classification": "Annual Salary",
                  "description": "Gross income is the total amount you earn (typically over the course of a year) before expenses. Net income is the profit your business earns after expenses ",
                  "information": "Depending on the home price you're aiming for, you may want to wait a year or two before you apply for a mortgage if you've just moved into a higher-paying role. The longer you stay in your higher-paying position, the more your lender may be willing to loan you.",
                  "note": "The amount of money you earn plays a smaller role in getting a mortgage than you might think. ",
                  "question": "What is your net monthly salary?",
                  "source": "https://www.rocketmortgage.com"
              }
          }
      }
      ```

#### Create a new education object
  - Method/HTTP_Verb: POST
  - `/api/v1/education`
  - Body:
    ```json
    {
      "classification": "", /* required && unique */
      "question": "", /* required */
      "description":  "", /* required */
      "information":  "",
      "note": "",
      "source": "" /* required */
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data

#### Update an education object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/education/<id>`
  - Body: You can update any of the following fields:
    ```json
    {
      "classification": "",
      "question": "",
      "description":  "",
      "information":  "",
      "note": "",
      "source": ""
    }
    ```
  - Returns:
    - The updated objects id with url for getting the updated object data


#### Destroy an education object by id
  - Method/HTTP_Verb: DELETE
  - `/api/v1/education/<id>`
  - Body: NA
  - Returns:
    - The destroyed objects id with url for getting the deletion confirmation for this object


## Report
---
<!-- #### Call all report objects
  - Method/HTTP_Verb: GET
  - `/api/v1/report`
  - Body: NA
  - Returns:
    - All report object id's
 -->
#### Call a single report object by id
  - Method/HTTP_Verb: GET
  - `/api/v1/report/<id>`
  - Body: NA
  - Returns:
    - A single report object's information
    - This is part of our MVP - our frontend can access a dynamic report response so they can display custom information to the user


#### Create a new report object
  - Method/HTTP_Verb: POST
  - `/api/v1/report`
  - Body:
    ```json
    {
      "salary": 0, /* required */
      "zipcode": 0, /* required */
      "credit_score": 0, /* required */
      "monthly_debt": 0, /* required */
      "downpayment_savings": 0, /* required */
      "downpayment_percentage": 0, /* required */
      "rent": 0, /* NOT required, but defaults to 0 if no input */
      "goal_principal": 0 /* NOT required, but defaults to 0 if no input */
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data


#### Update an report object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/report/<id>`
  - Body: You can update any of the following fields:
    ```json
    {
      "salary": 0,
      "zipcode": 0,
      "credit_score": 0,
      "monthly_debt": 0,
      "downpayment_savings": 0,
      "downpayment_percentage": 0,
      "rent": 0,
      "goal_principal": 0
    }
    ```
  - Returns:
    - The updated objects id with url for getting the updated object data


#### Destroy an report object by id
  - Method/HTTP_Verb: DELETE
  - `/api/v1/report/<id>`
  - Body: NA
  - Returns:
    - The destroyed objects id with url for getting the deletion confirmation for this object


## Property Tax
---
#### Call all property-tax objects
  - Method/HTTP_Verb: GET
  - `/api/v1/property-tax`
  - Body: NA
  - Returns:
    - A list of average property taxes by state

#### Call a single property-tax object by id
  - Method/HTTP_Verb: GET
  - `/api/v1/property-tax/<id>`
  - Body: NA
  - Returns:
    - A single property-tax object's information

#### Create a new property-tax object
  - Method/HTTP_Verb: POST
  - `/api/v1/property-tax`
  - Body:
    ```json
    {
      "state": "", /* required AND unique */
      "question": "", /* required */
      "description": "" /* required */
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data

#### Update an property-tax object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/property-tax/<id>`
  - Body: You can update any of the following fields:
    ```json
    {
      "state": "",
      "question": "",
      "description": ""
    }
    ```
  - Returns:
    - The updated objects id with url for getting the updated object data

#### Destroy an property-tax object by id
  - Method/HTTP_Verb: DELETE
  - `/api/v1/property-tax/<id>`
  - Body: NA
  - Returns:
    - The destroyed objects id with url for getting the deletion confirmation for this object


## PMI
---
#### Call all pmi objects
  - Method/HTTP_Verb: GET
  - `/api/v1/pmi`
  - Body: NA
  - Returns:
    - A list of PMI objects that represent different the LTV categories: 100 (0%), 95 (5%), 90 (10%), and 85 (15%)

#### Call a single pmi object by id
  - Method/HTTP_Verb: GET
  - `/api/v1/pmi/<id>`
  - Body: NA
  - Returns:
    - A single pmi object's information

#### Create a new pmi object
  - Method/HTTP_Verb: POST
  - `/api/v1/pmi`
  - Body:
    ```json
    {
      "downpayment_percentage": "", /* required AND unique */
      "range_620_639": "", /* required */
      "range_640_659": "", /* required */
      "range_660_679": "", /* required */
      "range_680_699": "", /* required */
      "range_700_719": "", /* required */
      "range_720_739": "", /* required */
      "range_740_759": "", /* required */
      "range_760_850": "" /* required */
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data

#### Update an pmi object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/pmi/<id>`
  - Body: You can update any of the following fields:
    ```json
    {
      "downpayment_percentage": "",
      "range_620_639": "",
      "range_640_659": "",
      "range_660_679": "",
      "range_680_699": "",
      "range_700_719": "",
      "range_720_739": "",
      "range_740_759": "",
      "range_760_850": ""
    }
    ```
  - Returns:
    - The updated objects id with url for getting the updated object data

#### Destroy an pmi object by id
  - Method/HTTP_Verb: DELETE
  - `/api/v1/pmi/<id>`
  - Body: NA
  - Returns:
    - The destroyed objects id with url for getting the deletion confirmation for this object


## Home Insurance
---
#### Call all home-insurance objects
  - Method/HTTP_Verb: GET
  - `/api/v1/home-insurance`
  - Body: NA
  - Returns:
    - A list of average home insurance by state

#### Call a single home-insurance object by id
  - Method/HTTP_Verb: GET
  - `/api/v1/home-insurance/<id>`
  - Body: NA
  - Returns:
    - A single home-insurance object's information

#### Create a new home-insurance object
  - Method/HTTP_Verb: POST
  - `/api/v1/home-insurance`
  - Body:
    ```json
    {
      "state": "", /* required AND unique */
      "annual_average_insurance_rate": "" /* required */
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data

#### Update an home-insurance object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/home-insurance/<id>`
  - Body: You can update any of the following fields:
    ```json
    {
      "state": "",
      "annual_average_insurance_rate": ""
    }
    ```
  - Returns:
    - The updated objects id with url for getting the updated object data

#### Destroy an home-insurance object by id
  - Method/HTTP_Verb: DELETE
  - `/api/v1/home-insurance/<id>`
  - Body: NA
  - Returns:
    - The destroyed objects id with url for getting the deletion confirmation for this object
