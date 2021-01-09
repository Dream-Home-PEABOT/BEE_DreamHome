# Brainstorm for API End Points of Education Model

The following endpoints can be asked in any order, except for the section titled "Last Question"

## Survey
GET http://localhost:5000/api/v1/education/survey
```json
{"data": {
  "annual_salary":{
    "question": "What is your net monthly salary?",
    "description": "soijrwofija;oijnfv;oi",
    "definition": "Define net here",
    "source": "http://www.example.com"
  },
  "zipcode":{
    "question": "What is the zipcode you'd like to live in?",
    "description": "ae;osihrf;oijaef",
    "source": "http://www.example.com"
  },
  "monthly_debt": {
    "question": "What is the zipcode you'd like to live in?",
    "description": "ae;osihrf;oijaef",
    "source": "http://www.example.com"
  },
  "downpayment_savings": {
    "question": "Do you have any savings set aside for your downpayment?",
    "description": "werfwerfwer",
    "source": ""
  },
  "credit_score_range":{
    "question": "What range does your credit score fall under?",
    "description": "aijsdfijfd",
    "source": ""
  },
  "downpayment_percentage": {
    "question": "What downpayment percentage are you aiming to save?",
    "description": "",
    "definition": "The national average is 20%, but many programs can support alternate percentages.",
    "source": ""
  },
  "mortgage_term": {
    "question": "What mortgage term are you aiming for?",
    "description": "",
    "definition": "Typically, a fixed-rate mortgage runs 30 years.",
    "source": ""
  },
  "rent": {
    "question": "IMAGINATIVE: What is your current monthly rent?",
    "description": "",
    "definition": "The imaginative report gives a total home price you can afford based off of your monthly rent.",
    "source": ""
  },
  "goal_home_price": {
    "question": "PRAGMATIC: What is the price of your ideal home?",
    "description": "",
    "definition": "The pragmatic report gives your monthly payment you would make with your goal price.",
    "source": ""
  },
  "external_services": {
    "property_tax": "number",
    "affordability": "mortgage amount + average mortgage from zipcode"
  }
}}
```

COMING SOON /REPORT
```json
"decade": {
  "1yr": {"monthly_goal": "1901.00", "purchase_date": "01/04/2022"},
  "2yr": {"monthly_goal": "1901.00", "purchase_date": "01/04/2023"},
  "3yr": {"monthly_goal": "1901.00", "purchase_date": "01/04/2024"},
  "4yr": {"monthly_goal": "1901.00", "purchase_date": "01/04/2025"},
  "5yr": {"monthly_goal": "1901.00", "purchase_date": "01/04/2026"},
  "6yr": {"monthly_goal": "1901.00", "purchase_date": "01/04/2027"},
  "7yr": {"monthly_goal": "1901.00", "purchase_date": "01/04/2028"},
  "8yr": {"monthly_goal": "1901.00", "purchase_date": "01/04/2029"},
  "9yr": {"monthly_goal": "1901.00", "purchase_date": "01/04/2030"},
  "10yr": {"monthly_goal": "1901.00", "purchase_date": "01/04/2031"}
}
```

## Salary
GET http://localhost:5000/api/v1/education/salary
```json
{
  "question": "What is your net monthly salary?",
  "description": "soijrwofija;oijnfv;oi",
  "definition": "Define net here",
  "source": "http://www.example.com"
}
```

## Zipcode
GET http://localhost:5000/api/v1/education/zipcode
```json
{
  "question": "What is the zipcode you'd like to live in?",
  "description": "ae;osihrf;oijaef",
  "source": "http://www.example.com"
}
```
## Monthly Debt
GET http://localhost:5000/api/v1/education/monthly-debt
```json
{
  "question": "What is your monthly debt?",
  "description": "",
  "definition": "Only things reported to credit score",
  "source": ""
}
```

## Downpayment Savings
GET http://localhost:5000/api/v1/education/downpayment-savings

 - Default downpayment savings is 0, if not given.

```json
{
  "question": "Do you have any savings set aside for your downpayment?",
  "description": "werfwerfwer",
  "source": ""
}
```
## Credit Score Range
GET http://localhost:5000/api/v1/education/credit-score-range
- Frontend has four ranges provided as radio buttons or dropdowns:
    - `350 - 629`
    - `630 - 689`
    - `690 - 719`
    - `720 - 850`
- Default range is 630-689, if not given.
```json
{
  "question": "What range does your credit score fall under?",
  "description": "aijsdfijfd",
  "source": ""
}
```
## What Downpayment Percent
GET http://localhost:5000/api/v1/education/downpayment-percentage
- Frontend has five options provided as radio buttons or dropdowns:
    - 0, 5, 10, 15, 20
    - Default downpayment percent is 20%, if not given.
```json
{
  "question": "What downpayment percentage are you aiming to save?",
  "description": "",
  "definition": "The national average is 20%, but many programs can support alternate percentages.",
  "source": ""
}
```

## Mortgage Term
GET http://localhost:5000/api/v1/education/mortgage-term
- - Frontend has three options provided as radio buttons or dropdowns:
    - 10 years, 15 years, 30 years
    - default will be 30 years

```json
{
  "question": "What mortgage term are you aiming for?",
  "description": "",
  "definition": "Typically, a fixed-rate mortgage runs 30 years.",
  "source": ""
}
```

## Last Question
### What rent?
GET http://localhost:5000/api/v1/education/rent
```json
{
  "question": "IMAGINATIVE: What is your current monthly rent?",
  "description": "",
  "definition": "The imaginative report gives a total home price you can afford based off of your monthly rent.",
  "source": ""
}
```
### Goal home price
GET http://localhost:5000/api/v1/education/goal-home-price
```json
{
  "question": "PRAGMATIC: What is the price of your ideal home?",
  "description": "",
  "definition": "The pragmatic report gives your monthly payment you would make with your goal price.",
  "source": ""
}
```
