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

    def index(self):
        all_pmi = Pmi.objects()

        json_pmi_objects = {}

        for pmi in all_pmi:
            json_pmi_objects[f'downpayment_{pmi.downpayment_percentage}'] = {
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

        return { "data": json_pmi_objects}, 200

    def update_pmi(self, id):
        pmi = Pmi.objects.get(id=id)
        body = request.get_json()
        pmi.update(**body)
        return {
            "data": {
                "id": str(id),
                "confirmation": {
                    "info": "To see this record's updated response, please do a GET request using the url",
                    'url': f'/api/v1/pmi/{id}'
                }
            }
        }, 200

    def destroy_pmi(self, id):
        pmi = Pmi.objects.get(id=id)
        pmi.delete()
        return {
            "data": {
                "id": 'nil',
                "confirmation": {
                    "info": "To see this record's deletion response, please do a GET request using the url",
                    "url": f'/api/v1/pmi{id}'
                }
            }
        }, 200

pmicontroller = PmiController()
