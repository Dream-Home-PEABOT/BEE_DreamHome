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


## Team Contributions Iteration 1
- [Priya Power](https://github.com/priyapower): Backend Algorithm Lead, Report Debugging Extraordinaire, Robust Testing Lead
- [Arique Aguilar](https://github.com/Arique1104): Backend RESTful API Lead, National Coverage for Home Insurance, Median Home Value, and Property Tax


## Team Contributions
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
    {
      "data": {
            "credit_score": {
                "01_type": "Education object",
                "02_id": "601216f2156bdf5d9ff712bb",
                "03_attributes": {
                    "A_order": 2,
                    "B_classification": "Credit Score",
                    "C_question": "What is your current credit score?",
                    "D_description": " A high score will give you access to lower interest rates and more lender choices. If you have a low score, you may have trouble getting a loan.",
                    "E_information": "Your credit score plays a big role in the interest rate you’ll get for your loan.",
                    "F_note": "Your credit score is a numerical rating that ranges from 300 – 850 and tells lenders how responsible you are when you borrow money. ",
                    "G_source": "https://www.rocketmortgage.com",
                    "H_symbol": ""
                }
            },
            "downpayment_percentage": {
                "01_type": "Education object",
                "02_id": "60121717165875de9b91bad0",
                "03_attributes": {
                    "A_order": 7,
                    "B_classification": "Downpayment Percentage",
                    "C_question": "What downpayment percentage are you aiming to save?",
                    "D_description": "Your down payment is the amount of money you put down on your mortgage. Your down payment is due during closing and is usually the most expensive closing cost you need to plan for.",
                    "E_information": "You might have heard you need 20% down to buy a home. The reason why this number is often quoted is that 20% down is the minimum you’ll need to avoid buying private mortgage insurance – it’s not the minimum you need to get a loan.",
                    "F_note": "You can buy a home with as little as 3% down.",
                    "G_source": "https://www.rocketmortgage.com",
                    "H_symbol": "%"
                }
            },
              ...
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
            "01_type": "Education object",
            "02_id": "60121717165875de9b91bad0",
            "03_attributes": {
                "A_order": 7,
                "B_classification": "Downpayment Percentage",
                "C_question": "What downpayment percentage are you aiming to save?",
                "D_description": "Your down payment is the amount of money you put down on your mortgage. Your down payment is due during closing and is usually the most expensive closing cost you need to plan for.",
                "E_information": "You might have heard you need 20% down to buy a home. The reason why this number is often quoted is that 20% down is the minimum you’ll need to avoid buying private mortgage insurance – it’s not the minimum you need to get a loan.",
                "F_note": "You can buy a home with as little as 3% down.",
                "G_source": "https://www.rocketmortgage.com",
                "H_symbol": "%"
            }
        }
    }
    ```

#### Create a new education object
  - Method/HTTP_Verb: POST
  - `/api/v1/education`
  - Body:
    ```py
    {
        "order": 2, # Required && Unique
        "classification": "Credit Score", # Required
        "question": "What is your curr...", # Required
        "description": " A high score ...", # Required
        "information": "Your credit score pl.", # Optional
        "note": "Your credit score is a numer", # Optional
        "source": "https://www.rocketmortgage.com",# Required
        "symbol": "" #Optional && Default=""
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data

#### Update an education object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/education/<id>`
  - Body: You can update any of the following fields:
    ```py
    {
        "order": 2, # Required && Unique
        "classification": "Credit Score", # Required
        "question": "What is your curr...", # Required
        "description": " A high score ...", # Required
        "information": "Your credit score pl.", # Optional
        "note": "Your credit score is a numer", # Optional
        "source": "https://www.rocketmortgage.com",# Required
        "symbol": "" #Optional && Default=""
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
    ```py
    {
        "zipcode": "80209", # Required
        "credit_score": 710, # Required
        "salary": 5000, # Required
        "monthly_debt": 1500, # Required
        "downpayment_savings": 50000, # Required
        "mortgage_term": 30, # Optional && Default=0
        "downpayment_percentage": 20, # Required
        "goal_principal": 500000, # Optional && Default=0
        "rent": 0 # Optional && Default=0
        "uid": # Optional
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data


#### Update an report object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/report/<id>`
  - Body: You can update any of the following fields:
    ```py
    {
        "zipcode": "80209", # Add Update
        "credit_score": 710, # Add Update
        "salary": 5000, # Add Update
        "monthly_debt": 1500, # Add Update
        "downpayment_savings": 50000, # Add Update
        "mortgage_term": 30, # Add Update
        "downpayment_percentage": 20, # Add Update
        "goal_principal": 500000, # Add Update
        "rent": 0, # Add Update
        "uid": 'lskijnvijfsis' # Add Update
    }
    ```
  - Returns:
    - The updated objects id with url for getting the updated object data

#### Assign UID to a report object
  - Method/HTTP_Verb: POST
  - `/api/v1/report/unique`
  - Body: You can update any of the following fields:
    ```py
    {
        "uid": 'fakejmsodicjuid'# Required
    }
    ```
  - Returns:
    - A report now linked with a registered users UID

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
        "state": "Colorado", # Required && Unique
        "avg_tax_rate": 0.53, # Required
        "annual_avg_property_tax": 1647 # Required
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data

#### Update an property-tax object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/property-tax/<id>`
  - Body: You can update any of the following fields:
    ```py
    {
        "state": "Colorado", # Add Update
        "avg_tax_rate": 0.53, # Add Update
        "annual_avg_property_tax": 1647 # Add Update
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
  ```py
    {
        "data": {
            "downpayment_0": {
                "attributes": {
                    "downpayment_percentage": 0,
                    "range_620_639": 2.25,
                    "range_640_659": 2.05,
                    "range_660_679": 1.9,
                    "range_680_699": 1.4,
                    "range_700_719": 1.15,
                    "range_720_739": 0.95,
                    "range_740_759": 0.75,
                    "range_760_850": 0.55
                },
                "id": "60121a06156bdf5d9ff712c4",
                "type": "Pmi object"
            },
            ...
        }
    }
  ```

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
    ```py
    {
        "downpayment_percentage": 0, # Required && Unique
        "range_620_639": 2.25, # Required
        "range_640_659": 2.05, # Required
        "range_660_679": 1.90, # Required
        "range_680_699": 1.4, # Required
        "range_700_719": 1.15, # Required
        "range_720_739": 0.95, # Required
        "range_740_759": 0.75, # Required
        "range_760_850": 0.55 # Required
    }
    ```
  - Returns:
    - The created objects id with url for getting the new object data

#### Update an pmi object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/pmi/<id>`
  - Body: You can update any of the following fields:
    ```py
    {
        "downpayment_percentage": 0, # Add Update
        "range_620_639": 2.25, # Add Update
        "range_640_659": 2.05, # Add Update
        "range_660_679": 1.90, # Add Update
        "range_680_699": 1.4, # Add Update
        "range_700_719": 1.15, # Add Update
        "range_720_739": 0.95, # Add Update
        "range_740_759": 0.75, # Add Update
        "range_760_850": 0.55 # Add Update
    }
    ```
  - Returns:
    - The updated objects id with url for getting the updated object data

#### Destroy a pmi object by id
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
    ```py
  {
      "state": "Colorado", # Required && Unique
      "annual_average_insurance_rate": 3082 # Required
  }
    ```
  - Returns:
    - Creates a single  home-insurance object's information

#### Update an home-insurance object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/home-insurance/<id>`
  - Body: You can update any of the following fields:
    ```py
    {
      "state": "Colorado", # Update
      "annual_average_insurance_rate": 3082 # Update
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

## Median Home Value
---
#### Call all median-home-value objects
  - Method/HTTP_Verb: GET
  - `/api/v1/median-home-value`
  - Body: NA
  - Returns:
    - A list of median home values by state

#### Call a single median-home-value object by id
  - Method/HTTP_Verb: GET
  - `/api/v1/median-home-value/<id>`
  - Body: NA
  - Returns:
    - A single median-home-value object's information

#### Create a new median-home-value object
  - Method/HTTP_Verb: POST
  - `/api/v1/median-home-value`
  - Body:
    ```py
  {
      "year": 2020, # Required
      "state": "Colorado", # Required && Unique
      "avg_home_value": 412819, # Required
      "median_top_tier": 642646, # Optional
      "median_single_family_value": 422369, # Optional
      "median_bottom_tier": 279396, # Optional
      "median_condo_value": 315402 # Optional
  }
    ```
  - Returns:
    - Creates a single median-home-value object's information

#### Update an median-home-value object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/median-home-value/<id>`
  - Body: You can update any of the following fields:
    ```py
    {
      "year": 2020, # Required
      "state": "Colorado", # Required && Unique
      "avg_home_value": 412819, # Required
      "median_top_tier": 642646, # Optional
      "median_single_family_value": 422369, # Optional
      "median_bottom_tier": 279396, # Optional
      "median_condo_value": 315402 # Optional
    }
    ```
  - Returns:
    - The updated objects id with url for getting the updated object data

#### Destroy an median-home-value object by id
  - Method/HTTP_Verb: DELETE
  - `/api/v1/median-home-value/<id>`
  - Body: NA
  - Returns:
    - The destroyed objects id with url for getting the deletion confirmation for this object


## Mortgage Rate
---
#### Call all median-home-value objects
  - Method/HTTP_Verb: GET
  - `/api/v1/mortgage-rate`
  - Body: NA
  - Returns:
    - A list of median home values by state

#### Call a single mortgage-rate object by id
  - Method/HTTP_Verb: GET
  - `/api/v1/mortgage-rate/<id>`
  - Body: NA
  - Returns:
    - A single mortgage-rate object's information

#### Create a new mortgage-rate object
  - Method/HTTP_Verb: POST
  - `/api/v1/mortgage-rate`
  - Body:
    ```py
  {
      "credit_score_floor": "700", # Required & Unique
      "credit_score_ceiling": "759", # Required & Unique
      "rate": 2.76 # Required
  }
    ```
  - Returns:
    - Creates a single mortgage-rate object's information

#### Update an mortgage-rate object by id
  - Method/HTTP_Verb: PUT
  - `/api/v1/mortgage-rate/<id>`
  - Body: You can update any of the following fields:
    ```py
  {
      "credit_score_floor": "700", # Update Info
      "credit_score_ceiling": "759", # Update Info
      "rate": 2.76 # Update Info
  }
    ```
  - Returns:
    - The updated objects id with url for getting the updated object data

#### Destroy an mortgage-rate object by id
  - Method/HTTP_Verb: DELETE
  - `/api/v1/mortgage-rate/<id>`
  - Body: NA
  - Returns:
    - The destroyed objects id with url for getting the deletion confirmation for this object
