# - post report,
{
"zipcode": 80209,  # 02115 (Boston)
"credit_score": 710,
"salary": 5000,
"monthly_debt": 1500,
"downpayment_savings": 50000,
"mortgage_term": 30,
"downpayment_percentage": 20,
"goal_principal": 500000,
"rent": 0,
"uid": 'wioejnfosijnwfvoijerowef12345'
}
# - get report by id

# - or put a uid and unique report
{"uid": 'wioejnfosijnwfvoijerowef12345'}


# Five things to load
  # mortgage-rate
  {
      "credit_score_floor": "700",
      "credit_score_ceiling": "759",
      "rate": 2.76
  }

  # pmi # won't need to pre-load pmi
  # home-insurance
  {
      "state": "Colorado",
      "annual_average_insurance_rate": 3082
  }

  # property-tax
  {
      "state": "Colorado",
      "avg_tax_rate": 0.53,
      "annual_avg_property_tax": 1647
  }

  # median-home-value
  {
      "year": 2020,
      "state": "Colorado",
      "avg_home_value": 412819,
      "median_top_tier": 642646,
      "median_single_family_value": 422369,
      "median_bottom_tier": 279396,
      "median_condo_value": 315402
  }

  # post /report
  # report
  {
  "zipcode": 80209,
  "credit_score": 710,
  "salary": 5000,
  "monthly_debt": 1500,
  "downpayment_savings": 50000,
  "mortgage_term": 30,
  "downpayment_percentage": 20,
  "goal_principal": 500000,
  "rent": 0
  }
