from flask import Response, request, render_template
from api.models.property_tax import PropertyTax
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from re import sub
import pry

class PropertyTaxController():
    # single Get
    def get_property_tax(self, id):
        tax_info = PropertyTax.objects.get(id=id)
        return {
            "data": {
                "type": str(tax_info),
                "id": str(tax_info.id),
                "attributes": {
                    "state": tax_info.state,
                    "tax_rate": tax_info.tax_rate,
                    "avg_property_tax": tax_info.avg_property_tax
                }
            }
        }, 200

    def add_property_tax(self):
        # try:
        body = request.get_json()
        property_tax = PropertyTax(**body)
        property_tax.save()
        id = property_tax.id
        return {
            "data": {
                "id": str(id),
                "confirmation": {
                    "info": 'To see this new record, please do a GET request using the url',
                    "url": f'/api/v1/property_tax/{id}'
                }
            }
        }, 200

    def index(self):
        all_property_tax = PropertyTax.objects()

        def convert_snake(string):
            return '_'.join(
                sub('([A-Z][a-z]+)', r' \1',
                sub('([A-Z]+)', r' \1',
                string.replace('-', ' '))).split()).lower()

        json_property_tax_objects = {}
        for propertytax in all_property_tax:
            json_property_tax_objects[convert_snake(propertytax.state)] = {
                "type": str(propertytax),
                "id": str(propertytax.id),
                "attributes": {
                    "state": propertytax.state,
                    "tax_rate": propertytax.tax_rate,
                    "avg_property_tax_rate": propertytax.avg_property_tax_rate,
                }
            }
    
        return {"data": json_property_tax_objects}, 200


propertytaxcontroller = PropertyTaxController()
