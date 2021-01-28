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
        'host': 'mongodb://localhost/dreamhome-test'
    }
    ```
  - To run all tests: `python -m unittest -b`
  - To run a single test: `python -m unittest tests/test_<file_name>.py`
  - To run coverage: `coverage run -m unittest discover`
  - To open coverage report: `open html cov/index.html` OR `coverage report -m` OR `coverage html`

## .env vs .env.test!!!

## Tech stack
- [Python](https://www.python.org)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [MongoDB](https://www.mongodb.com)
- [MongoEngine](http://mongoengine.org)
- [Mongo Atlas](https://www.mongodb.com/cloud/atlas)
- [noSQL](https://en.wikipedia.org/wiki/NoSQL)
- [Heroku](https://www.heroku.com)
- [JSON](https://jsonapi.org)

## Team Contributions Iteration 1
- [Priya Power](https://github.com/priyapower): Backend Team Lead, Developer, Researcher, Backend Learning Coach
- [Arique Aguilar](https://github.com/Arique1104): Backend Developer, Deployment Guru, Frontend Liaison and Design Consultant


## Team Contributions MVP
- [Priya Power](https://github.com/priyapower): Backend Team Lead, Developer, Researcher, Backend Learning Coach
- [Arique Aguilar](https://github.com/Arique1104): Backend Developer, Deployment Guru, Frontend Liaison and Design Consultant
- [Eric Hale](https://github.com/EHale64): Backend Developer, Web Scraping Researcher

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
    ADD NEW EDUCATION RESPONSE HERE!
      ```

#### Call a single education object by id
  - Method/HTTP_Verb: GET
  - `/api/v1/education/<id>`
  - Body: NA
  - Returns:
    - A single education object's information
    - Example response:
      ```json
    ADD NEW EDUCATION RESPONSE HERE!

      ```

#### Create a new education object
  - Method/HTTP_Verb: POST
  - `/api/v1/education`
  - Body:
    ```
    {
      "classification": String, # required && unique,
      "question": String, # required
      "description": String, # required
      "information":  String, # optional
      "note": String, # optional
      "source": required,
      "order": required,
      "symbol": optional
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data

#### Update an education object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/education/<id>`
  - Body: You can update any of the following fields:
    ```
    {
      "classification": "add updated information here",
      "question": "add updated information here",
      "description": "add updated information here",
      "information":  "add updated information here",
      "note": "add updated information here",
      "source": "add updated information here",
      "order": "add updated information here",
      "symbol": "add updated information here"l
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
    ```
    {
      "zipcode": Integer (required=True),
      "credit_score": Integer (required=True),
      "salary": Integer (required=True),
      "monthly_debt": Integer (required=True),
      "downpayment_savings": Integer (required=True),
      "mortgage_term": Integer(default=0),
      "downpayment_percentage": Integer (required=True),
      "goal_principal": Integer (default=0),
      "rent": Integer (default=0)
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data


#### Update an report object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/report/<id>`
  - Body: You can update any of the following fields:
    ```
    {
      "zipcode": Add updated info (required=True),
      "credit_score": Add updated info (required=True),
      "salary": Add updated info (required=True),
      "monthly_debt": Add updated info (required=True),
      "downpayment_savings": Add updated info (required=True),
      "mortgage_term": Add updated info(default=0),
      "downpayment_percentage": Add updated info (required=True),
      "goal_principal": Add updated info (default=0),
      "rent": Add updated info (default=0)
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
    ```py
    {
      "state": "", # required AND unique
      "question": "", # required
      "description": "" # required
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
