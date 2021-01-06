# DreamHome BackEnd


## About

## Setup Instructions
  - how to run the dev/test server locally
  - how to run production deployed server

## Visual Schema
- Report Model
```
User clicks sumbit on survey
# POST http://localhost:5000/report
{
  salary: 55000,
  zipcode: 11111,
  credit: 695,
  monthly_debt: 1100,
  downpayment_savings: 10000,
  downpayment_percentage: 10,
  rent: 1800,
  goal_principal: 0
}
# The following is the json return to the POST from above
{
  report: {
    location: {
      zip_code: 11111,
      location: "Anywhere, CO",
    },
    principal: {
      based_on_rent: 350000,
      goal_principal: 0
    },
    monthly: {
      monthly_principal: 1400,
      estimated_true_monthly: 1940,
      add_ons: {
        home_insurance: 110,
        property_tax: 105,
        hoa: 75,
        pmi: 250
      }
    },
    downpayment: {
      down_payment_percentage_selected: 10,
      down_payment_saved: 10000,
      down_payment_percent_saved: 2.9,
      ten_year_plan: {
        one: {
          monthly_savings: 100,
          goal_end_date: 12/03/2022
        },
        two: {
          monthly_savings: 100,
          goal_end_date: 12/03/2023
        },
        three: {
          monthly_savings: 100,
          goal_end_date: 12/03/2024
        },
        four: {
          monthly_savings: 100,
          goal_end_date: 12/03/2025
        },
        five: {
          monthly_savings: 100,
          goal_end_date: 12/03/2026
        },
        six: {
          monthly_savings: 100,
          goal_end_date: 12/03/2027
        },
        seven: {
          monthly_savings: 100,
          goal_end_date: 12/03/2028
        },
        eight: {
          monthly_savings: 100,
          goal_end_date: 12/03/2029
        },
        nine: {
          monthly_savings: 100,
          goal_end_date: 12/03/2030
        },
        ten: {
          monthly_savings: 100,
          goal_end_date: 12/03/2031
        }
      }
    }
  }
}
```

Education
```
const data = {
  "data": {
  "annual_salary":{
    "classification": "Annual Salary",
    "question": "What is your net monthly salary?",
    "description": "Gross income is the total amount you earn (typically over the course of a year) before expenses. Net income is the profit your business earns after expenses ",
    "information": "Depending on the home price you’re aiming for, you may want to wait a year or two before you apply for a mortgage if you’ve just moved into a higher-paying role. The longer you stay in your higher-paying position, the more your lender may be willing to loan you.",
    "note":"The amount of money you earn plays a smaller role in getting a mortgage than you might think. ",
    "source": "https://www.rocketmortgage.com"
  },
  "zipcode":{
    "classification": "ZIP Code",
    "question": "What is the zipcode you'd like to live in?",
    "description":"Property taxes and interest rates can vary by location. Enter the ZIP code where you're looking for homes and we'll automatically add property taxes and interest rates for your area.",
    "information": "A “cost of living analysis” by two large realty companies discovered that living in the suburbs versus living in the city does impact your cost of living – by thousands of dollars. ",
    "note": "The term ZIP is an acronym for Zone Improvement Plan",
    "source": "http://www.trulia.com/"
  },
  "monthly_debt": {
    "classification": "Monthly Debt",
    "question": "What would you say your monthly debt is?",
    "description": "What to include: Minimum credit card payment, Auto, student, or personal loan payments,Alimony or child support, Do not include: Current rent or mortgage Credit card balances Monthly utilities, groceries, and other costs of living",
    "information":"This is NOT your DTI aka Debt-To-Income Ratio, Your DTI is equal to your total fixed, recurring monthly debts divided by your total monthly gross household income.",
    "note": "Your debts directly affect your affordability, since it’s based on the ratio between what you earn (income) and what you owe (debts).",
    "source": "http://www.trulia.com"
  },
  "downpayment_savings": {
    "classification": "Downpayment Savings",
    "question": "Do you have any savings set aside for your downpayment?",
    "description": "Your down payment plays a big part in your affordability. The more you put down, the lower your monthly payment will be.",
    "information": "That money typically comes from your personal savings, and in most cases, you pay with a check, a credit card, or an electronic payment.",
    "note":"Homeownership comes with costs that rentals do not. So remember to put extra money away for repairs and maintenance.",
    "source": "http://www.trulia.com"
  },
  "credit_score_range":{
    "classification": "Credit Score",
    "question": "What is your current credit score?",
    "description": " A high score will give you access to lower interest rates and more lender choices. If you have a low score, you may have trouble getting a loan.",
    "information": "Your credit score plays a big role in the interest rate you’ll get for your loan.",
    "note": "Your credit score is a numerical rating that ranges from 300 – 850 and tells lenders how responsible you are when you borrow money. ",
    "source": "https://www.rocketmortgage.com"
  },
  "downpayment_percentage": {
    "classification": "Downpayment Percentage",
    "question": "What downpayment percentage are you aiming to save?",
    "definition": "Your down payment is the amount of money you put down on your mortgage. Your down payment is due during closing and is usually the most expensive closing cost you need to plan for.",
    "information": "You might have heard you need 20% down to buy a home. The reason why this number is often quoted is that 20% down is the minimum you’ll need to avoid buying private mortgage insurance – it’s not the minimum you need to get a loan.",
    "note":"You can buy a home with as little as 3% down.",
    "source": "https://www.rocketmortgage.com"
  },
  "mortgage_term": {
    "classification": "Mortgage Term",
    "question": "What mortgage term are you aiming for?",
    "description": "Your mortgage term is the number of years you’ll pay on your loan before you fully own your home. ",
    "information": "A mortgage is a classification of loan that uses your home as collateral. It’s typically used to buy a home or in refinance situations to secure a more favorable deal and possibly convert equity in your home to cash.",
    "note": "Typically, a fixed-rate mortgage runs 30 years and this is the number we will use if you want us to.",
    "source": "https://www.rocketmortgage.com/"
  },
  "rent": {
    "classification": "Rent",
    "question": "IMAGINATIVE: What is your current monthly rent?",
    "description": "",
    "information": "",
    "note": "The imaginative report gives a total home price you can afford based off of your monthly rent.",
    "source": ""
  },
  "goal_home_price": {
    "classification": "Goal Home Price",
    "question": "PRAGMATIC: What is the price of your ideal home?",
    "description": "",
    "information": "",
    "note": "The pragmatic report gives your monthly payment you would make with your goal price.",
    "source": ""
  },
  "external_services": {
    "classification": "",
    "property_tax": "number",
    "description": "",
    "information": "",
    "note":"",
    "affordability": "mortgage amount + average mortgage from zipcode"
  },
  "survey":{
    "classification": "survey",
    "question": "",
    "description": "While every person’s situation is different we aim to provide you with a report that would give you a better perspective on where you are on your dream home quest. We based our data on your net monthly income (that’s after taxes), monthly debt, income, downpayment and more",
    "information": "One of the main questions to answers is how much can I afford?. Affordability is defined as the cost of something.",
    "note": "Here are the generally recommended guidelines: * Your mortgage payment should be 28% or less. * Your debt-to-income ratio (DTI) should be 36% or less. * Your housing expenses should be 29% or less. This is for things like insurance, taxes, maintenance, and repairs. * You should have three months of housing payments and expenses saved up.",
    "source": "http://www.trulia.com"
  }
```
## Tech stack

## Development Database Instructions

## Endpoint Documentation

## File Tree
dreamhome_server
  - api
    - controller
      - Welcome/Documentation
      - Education
      - Results
    - models
      - Documentation
      - Education
      - Results
    - views
      - Welcome.html
    - routes
      - api_routes.py
      - welcome_routes.py
    - services
      - real_estate api
  - database
    - db.py
    - seed_education.json
    - seed_results.json
  - tests
    - test_*.py
  - Pipfile
  - .env
  - app.py
  - run.py
