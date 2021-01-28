from flask import Response, request
from api.models.report import User
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError
from re import sub
import pry


class UserController():

    def add_user(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.save()
            id = user.id
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": 'To see this new user, please do a GET request using the url',
                        "url": f'/api/v1/user/{id}'
                    }
                }
            }, 201
        except NotUniqueError:
            raise APINotUniqueError("A user with this email already exists in the database")
        except (FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the user documentation. Request is missing a required field or incorrect field entered.")
        except Exception:
            raise 500


usercontroller = UserController()
