# DreamHome BackEnd
___
## About
- _about_

## Setup Instructions
- how to run the dev/test server locally
- how to run production deployed server

## Visual Schema
- ![schema]()

## Tech stack
- _stack_

## Development Database Instructions
- _instructions_

## Education Endpoints
- `GET http://localhost:5000/api/v1/education`
  ```json
  {
      "data": {
          "annual_salary": {
              "attributes": {
                  "classification": "Annual Salary",
                  "description": "Gross income is the total amount you earn (typically over the course of a year) before expenses. Net income is the profit your business earns after expenses ",
                  "information": "Depending on the home price you’re aiming for, you may want to wait a year or two before you apply for a mortgage if you’ve just moved into a higher-paying role. The longer you stay in your higher-paying position, the more your lender may be willing to loan you.",
                  "note": "The amount of money you earn plays a smaller role in getting a mortgage than you might think. ",
                  "question": "What is your net monthly salary?",
                  "source": "https://www.rocketmortgage.com"
              },
              "id": "5ff7a737be8682d9e5b0e0c2",
              "type": "Education object"
          },
          "credit_score": {
              "attributes": {
                  "classification": "Credit Score",
                  "description": " A high score will give you access to lower interest rates and more lender choices. If you have a low score, you may have trouble getting a loan.",
                  "information": "Your credit score plays a big role in the interest rate you’ll get for your loan.",
                  "note": "Your credit score is a numerical rating that ranges from 300 – 850 and tells lenders how responsible you are when you borrow money. ",
                  "question": "What is your current credit score?",
                  "source": "https://www.rocketmortgage.com"
              },
              "id": "5ff7a752be8682d9e5b0e0c6",
              "type": "Education object"
          },
          "downpayment_percentage": {
              "attributes": {
                  "classification": "Downpayment Percentage",
                  "description": "Your down payment is the amount of money you put down on your mortgage. Your down payment is due during closing and is usually the most expensive closing cost you need to plan for.",
                  "information": "You might have heard you need 20% down to buy a home. The reason why this number is often quoted is that 20% down is the minimum you’ll need to avoid buying private mortgage insurance – it’s not the minimum you need to get a loan.",
                  "note": "You can buy a home with as little as 3% down.",
                  "question": "What downpayment percentage are you aiming to save?",
                  "source": "https://www.rocketmortgage.com"
              },
              "id": "5ff7a757be8682d9e5b0e0c7",
              "type": "Education object"
          },
          "downpayment_savings": {
              "attributes": {
                  "classification": "Downpayment Savings",
                  "description": "Your down payment plays a big part in your affordability. The more you put down, the lower your monthly payment will be.",
                  "information": "That money typically comes from your personal savings, and in most cases, you pay with a check, a credit card, or an electronic payment.",
                  "note": "Homeownership comes with costs that rentals do not. So remember to put extra money away for repairs and maintenance.",
                  "question": "Do you have any savings set aside for your downpayment?",
                  "source": "http://www.trulia.com"
              },
              "id": "5ff7a74bbe8682d9e5b0e0c5",
              "type": "Education object"
          },
          "goal_home_price": {
              "attributes": {
                  "classification": "Goal Home Price",
                  "description": "",
                  "information": "",
                  "note": "The pragmatic report gives your monthly payment you would make with your goal price.",
                  "question": "PRAGMATIC: What is the price of your ideal home?",
                  "source": ""
              },
              "id": "5ff7a6cd6584018579aea7e6",
              "type": "Education object"
          },
          "monthly_debt": {
              "attributes": {
                  "classification": "Monthly Debt",
                  "description": "What to include: Minimum credit card payment, Auto, student, or personal loan payments,Alimony or child support, Do not include: Current rent or mortgage Credit card balances Monthly utilities, groceries, and other costs of living",
                  "information": "This is NOT your DTI aka Debt-To-Income Ratio, Your DTI is equal to your total fixed, recurring monthly debts divided by your total monthly gross household income.",
                  "note": "Your debts directly affect your affordability, since it’s based on the ratio between what you earn (income) and what you owe (debts).",
                  "question": "What would you say your monthly debt is?",
                  "source": "http://www.trulia.com"
              },
              "id": "5ff7a745be8682d9e5b0e0c4",
              "type": "Education object"
          },
          "mortgage_term": {
              "attributes": {
                  "classification": "Mortgage Term",
                  "description": "Your mortgage term is the number of years you’ll pay on your loan before you fully own your home. ",
                  "information": "A mortgage is a classification of loan that uses your home as collateral. It’s typically used to buy a home or in refinance situations to secure a more favorable deal and possibly convert equity in your home to cash.",
                  "note": "Typically, a fixed-rate mortgage runs 30 years and this is the number we will use if you want us to.",
                  "question": "What mortgage term are you aiming for?",
                  "source": "https://www.rocketmortgage.com/"
              },
              "id": "5ff7a75ebe8682d9e5b0e0c8",
              "type": "Education object"
          },
          "rent": {
              "attributes": {
                  "classification": "Rent",
                  "description": "",
                  "information": "",
                  "note": "The imaginative report gives a total home price you can afford based off of your monthly rent.",
                  "question": "IMAGINATIVE: What is your current monthly rent?",
                  "source": ""
              },
              "id": "5ff7a764be8682d9e5b0e0c9",
              "type": "Education object"
          },
          "zip_code": {
              "attributes": {
                  "classification": "ZIP Code",
                  "description": "Property taxes and interest rates can vary by location. Enter the ZIP code where you're looking for homes and we'll automatically add property taxes and interest rates for your area.",
                  "information": "A “cost of living analysis” by two large realty companies discovered that living in the suburbs versus living in the city does impact your cost of living – by thousands of dollars. ",
                  "note": "The term ZIP is an acronym for Zone Improvement Plan",
                  "question": "What is the zipcode you'd like to live in?",
                  "source": "http://www.trulia.com/"
              },
              "id": "5ff7a73dbe8682d9e5b0e0c3",
              "type": "Education object"
          }
      }
  }
  ```
- `POST http://localhost:5000/api/v1/education/<id>`
- `GET http://localhost:5000/api/v1/education/<id>`
- `PUT http://localhost:5000/api/v1/education/<id>`
- `DELETE http://localhost:5000/api/v1/education/<id>`

### Report Model
#### REQUEST
```
User clicks submit on survey
# POST http://localhost:5000/api/v1/report
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
```

#### RESPONSE
```
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
