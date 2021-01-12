
```python
from database.db import db

class PMI(db.Document):
    downpayment_percentage = db.IntField(required=True, unique=True)
    620_639 = db.FloatField(required=True)
    640_659 = db.FloatField(required=True)
    660_679 = db.FloatField(required=True)
    680_699 = db.FloatField(required=True)
    700_719 = db.FloatField(required=True)
    720_739 = db.FloatField(required=True)
    740_759 = db.FloatField(required=True)
    760_850 = db.FloatField(required=True)
```

```python
class PMI(db.Document):
  downpayment_percentage = 0
  620_639 = 2.25
  640_659 = 2.05
  660_679 = 1.90
  680_699 = 1.4
  700_719 = 1.15
  720_739 = 0.95
  740_759 = 0.75
  760_850 = 0.55

class PMI(db.Document):
  downpayment_percentage = 5
  620_639 = 1.61
  640_659 = 1.5
  660_679 = 1.42
  680_699 = 1.08
  700_719 = 0.87
  720_739 = 0.73
  740_759 = 0.59
  760_850 = 0.41

class PMI(db.Document):
    downpayment_percentage = 10
    620_639 = 1.10
    640_659 = 1.05
    660_679 = 1.00
    680_699 = 0.73
    700_719 = 0.60
    720_739 = 0.50
    740_759 = 0.41
    760_850 = 0.30

class PMI(db.Document):
    downpayment_percentage = 15
    620_639 = 0.45
    640_659 = 0.43
    660_679 = 0.41
    680_699 = 0.32
    700_719 = 0.27
    720_739 = 0.23
    740_759 = 0.20
    760_850 = 0.19


"0%", "5%", "10%", "15%"
```

function math
```
x =  PMI annual MIP / 100

y = x * (Principal - Finaldownpayment)

estimatedmonthlyPMI = y / 12
```

PMI Object 1 = LTV 100 (0%) => PDF is 96.5
```json
{
  "data": {
    "type": blarg,
    "id": 12334,
    "attributes": {
      "downpayment_percentage": 0,
      "prop_tax": {
        "620-639": what+we_saving,
        "640-659": balshrejkjdsf,
        "620-639": what+we_saving,
        "640-659": balshrejkjdsf,
        "620-639": what+we_saving,
        "640-659": balshrejkjdsf
      }
    }
  }
}
```

PMI Object 2 = LTV 95 (5%)
```json
{
  "data": {
    "downpayment_zero": {
      "attributes": {
        "downpayment_percentage": 0,
        "prop_tax": {
          "620-639": what+we_saving,
          "640-659": balshrejkjdsf,
          "620-639": what+we_saving,
          "640-659": balshrejkjdsf,
          "620-639": what+we_saving,
          "640-659": balshrejkjdsf
    },
    "id": 12334,
    "type": "PMI Object"
  },
    "downpayment_five": {
          "attributes": {
            "downpayment_percentage": 5,
            "prop_tax": {
              "620-639": what+we_saving,
              "640-659": balshrejkjdsf,
              "620-639": what+we_saving,
              "640-659": balshrejkjdsf,
              "620-639": what+we_saving,
              "640-659": balshrejkjdsf
        },
        "id": 12334,
        "type": "PMI Object"
    },
    "downpayment_five": {
          "attributes": {
            "downpayment_percentage": 5,
            "prop_tax": {
              "620-639": what+we_saving,
              "640-659": balshrejkjdsf,
              "620-639": what+we_saving,
              "640-659": balshrejkjdsf,
              "620-639": what+we_saving,
              "640-659": balshrejkjdsf
        },
        "id": 12334,
        "type": "PMI Object"
    },
    "downpayment_five": {
          "attributes": {
            "downpayment_percentage": 5,
            "prop_tax": {
              "620-639": what+we_saving,
              "640-659": balshrejkjdsf,
              "620-639": what+we_saving,
              "640-659": balshrejkjdsf,
              "620-639": what+we_saving,
              "640-659": balshrejkjdsf
        },
        "id": 12334,
        "type": "PMI Object"
    }

      }
    }
  }
}
```
