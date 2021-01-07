class InternalServerError(Exception):
    pass
class SchemaValidationError(Exception):
    pass
class EducationAlreadyExistsError(Exception):
    pass
class UpdatingEducationError(Exception):
    pass
class DeletingEducationError(Exception):
    pass
class EducationNotExistsError(Exception):
    pass
class EmailAlreadyExistsError(Exception):
    pass
class UnauthorizedError(Exception):
    pass
class EmailDoesnotExistsError(Exception):
    pass
class BadTokenError(Exception):
    pass
errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "EducationAlreadyExistsError": {
         "message": "Education with given classification already exists",
         "status": 400
     },
     "UpdatingEducationError": {
         "message": "Updating Education is forbidden by non-admin users",
         "status": 403
     },
     "DeletingEducationError": {
         "message": "Deleting Education is forbidden by non-admin users",
         "status": 403
     },
     "EducationNotExistsError": {
         "message": "Education with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },
    "EmailDoesnotExistsError": {
        "message": "Couldn't find the user with given email address",
        "status": 400
    },
    "BadTokenError": {
        "message": "Invalid token",
        "status": 403
    }
}
