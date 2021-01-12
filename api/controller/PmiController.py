from flask import Response, request
from api.models.pmi import Pmi
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
import pry

class PmiController():

    def add_pmi(self):
        body = request.get_json()
        pmi = Pmi(**body)
        pmi.save()
        id = pmi.id
        return {
            "data": {
                "id": str(id),
                "confirmation": {
                    "info": 'To see this new record, please do a GET request using the url',
                    "url": f'/api/v1/pmi/{id}'
                }
            }
        }, 200

    def get_pmi(self, id):
        pmi = Pmi.objects.get(id=id)
        return {
            "data": {
                "type": str(pmi),
                "id": str(pmi.id),
                "attributes": {
                    "downpayment_percentage": pmi.downpayment_percentage,
                    "from_620_639": pmi.from_620_639,
                    "from_640_659": pmi.from_640_659,
                    "from_660_679": pmi.from_660_679,
                    "from_680_699": pmi.from_680_699,
                    "from_700_719": pmi.from_700_719,
                    "from_720_739": pmi.from_720_739,
                    "from_740_759": pmi.from_740_759,
                    "from_760_850": pmi.from_760_850
                }
            }
        }, 200



pmicontroller = PmiController()
