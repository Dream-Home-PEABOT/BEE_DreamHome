from flask import Response, request, render_template
from api.models.property_tax import PropertyTax
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError
from re import sub


class PropertyTaxController():
    # single Get
    def get_property_tax(self, id):
        try:
            tax_info = PropertyTax.objects.get(id=id)
            return {
                "data": {
                    "type": str(tax_info),
                    "id": str(tax_info.id),
                    "attributes": {
                        "state": tax_info.state,
                        "avg_tax_rate": tax_info.avg_tax_rate,
                        "annual_avg_property_tax": tax_info.annual_avg_property_tax
                    }
                }
            }, 200
        except  (ValidationError, DoesNotExist):
            raise APIDoesNotExistError("Please check your request, the Property Tax record with given id doesn't exist.")
        except Exception:
            raise 500
    # POST
    def add_property_tax(self):
        try:
            body = request.get_json()
            property_tax = PropertyTax(**body)
            property_tax.save()
            id = property_tax.id
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": 'To see this new record, please do a GET request using the url',
                        "url": f'/api/v1/property-tax/{id}'
                    }
                }
            }, 201
        except NotUniqueError:
            raise APINotUniqueError("This Tax record's classification already exists in the database")
        except (FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Property Tax documentation. Request is missing a required field or incorrect field entered.")
        except Exception:
            raise 500

    def index(self):
        try:
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
                        "avg_tax_rate": propertytax.avg_tax_rate,
                        "annual_avg_property_tax": propertytax.annual_avg_property_tax,
                    }
                }

            return {"data": json_property_tax_objects}, 200
        except Exception:
            raise 500

    # PUT
    def update_property_tax(self, id):
        try:
            property_tax = PropertyTax.objects.get(id=id)
            body = request.get_json()
            property_tax.update(**body)
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": "To see this record's update response, please do a GET request using the url",
                        "url": f'/api/v1/property-tax/{id}'
                    }
                }
            }, 202
        except (InvalidQueryError, FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Property Tax documentation. Request is missing a required field or incorrect field entered.")
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Tax record with given id doesn't exist.")
        except Exception:
            raise 500

     # DESTROY
    def destroy_property_tax(self, id):
        try:
            property_tax = PropertyTax.objects.get(id=id)
            property_tax.delete()
            return {
                "data": {
                    "id": 'nil',
                    "confirmation": {
                        "info": "To see this record's deletion response, please do a GET request using the url",
                        "url": f'/api/v1/property-tax/{id}'
                    }
                }
            }, 200
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Tax record with given id doesn't exist.")
        except Exception:
            raise 500
propertytaxcontroller = PropertyTaxController()
