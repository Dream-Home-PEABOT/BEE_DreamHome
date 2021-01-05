# Brainstorm for API End Points of Education Model
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
```json
{
  "question": "What range does your credit score fall under?",
  "description": "aijsdfijfd",
  "source": ""
}
```
## What Downpayment Percent
GET http://localhost:5000/api/v1/education/downpayment-percentage
- - Frontend has five options provided as radio buttons or dropdowns:
    - 0, 5, 10, 15, 20
```json
{
  "question": "What downpayment percentage are you aiming to save?",
  "description": "",
  "definition": "The national average is 20%, but many programs can support alternate percentages.",
  "source": ""
}
```
## Same Page
### What rent?
GET http://localhost:5000/api/v1/education/rent
```json
{
  "question": "IMAGINATIVE: What is your current monthly rent?",
  "description": "",
  "source": ""
}
```
### Goal home price
GET http://localhost:5000/api/v1/education/goal-home-price
```json
{
  "question": "PRAGMATIC: What is the price of your ideal home?",
  "description": "",
  "source": ""
}
```
