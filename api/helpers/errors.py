# 400 - Server cannot process request
# 401 - Authentication required or has failed
# 403 - Authorization level not met
# 404 - Not Found
# 405 - Incorrect HTTP Verb
# 406 - Input data is incorrectly formatted
# 410 - Empty resource
# 200 - Standard sucess
# 201 - Creates new resource
# 202 - Accepted information for processing (update)
# 204 - No Content (maybe this is delete)


class APIError(Exception):
    """All custom API Exceptions"""
    pass

# --------------------------CUSTOM CLASSES--------------------------

class APINotUniqueError(APIError):
    """Custom Record Not Unique Error Class."""
    code = 400
    description = "Not Unique Error"

class APISchemaError(APIError):
    """Custom Record Internal Server Error Class."""
    code = 406
    description = "Schema Error"

class APIDoesNotExistError(APIError):
    """Custom Record Internal Server Error Class."""
    code = 400
    description = "Does Not Exist Error"
