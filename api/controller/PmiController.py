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
        }, 201

    def get_pmi(self, id):
        pmi = Pmi.objects.get(id=id)
        return {
            "data": {
                "type": str(pmi),
                "id": str(pmi.id),
                "attributes": {
                    "downpayment_percentage": pmi.downpayment_percentage,
                    "range_620_639": pmi.range_620_639,
                    "range_640_659": pmi.range_640_659,
                    "range_660_679": pmi.range_660_679,
                    "range_680_699": pmi.range_680_699,
                    "range_700_719": pmi.range_700_719,
                    "range_720_739": pmi.range_720_739,
                    "range_740_759": pmi.range_740_759,
                    "range_760_850": pmi.range_760_850
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
                    "range_620_639": pmi.range_620_639,
                    "range_640_659": pmi.range_640_659,
                    "range_660_679": pmi.range_660_679,
                    "range_680_699": pmi.range_680_699,
                    "range_700_719": pmi.range_700_719,
                    "range_720_739": pmi.range_720_739,
                    "range_740_759": pmi.range_740_759,
                    "range_760_850": pmi.range_760_850
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
