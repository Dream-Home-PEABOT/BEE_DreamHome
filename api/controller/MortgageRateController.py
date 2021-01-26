from flask import Response, request
from api.models.mortgage_rate import MortgageRate
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError
from re import sub
import pry

class MortgageRateController():

    #single GET

    #GET all

    #POST

    #PUT

    #DELETE

mortgageratecontroller = MortgageRateController()
