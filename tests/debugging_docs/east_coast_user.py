# - post report,
{
"zipcode": "02115",
"credit_score": 710,
"salary": 5000,
"monthly_debt": 1500,
"downpayment_savings": 50000,
"mortgage_term": 30,
"downpayment_percentage": 20,
"goal_principal": 500000,
"rent": 0
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
    "state": "Massachusetts",
    "annual_average_insurance_rate": 1920
}

  # property-tax
 {
    "state": "Massachusetts",
    "avg_tax_rate": 1.23,
    "annual_avg_property_tax": 4508
}

  # median-home-value
{
    "year": 2020,
    "state": "Massachusetts",
    "avg_home_value": 439541,
    "median_top_tier": 732598,
    "median_single_family_value": 447367,
    "median_bottom_tier": 283343,
    "median_condo_value": 393196
}
