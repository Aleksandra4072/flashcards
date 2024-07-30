from fastapi import HTTPException


class Error401(HTTPException):
    def __init__(self, details: str = None):
        super().__init__(401, detail=[{"message": "Received an unauthorized request", "details": details}])


class Error400(HTTPException):
    def __init__(self, details: str = None):
        super().__init__(400, detail=[{"message": "Something went wrong", "details": details}])


class Error403(HTTPException):
    def __init__(self, details: str = None):
        super().__init__(403, detail=[{"message": "Access denied", "details": details}])


class Error404(HTTPException):
    def __init__(self, details: str = None):
        super().__init__(403, detail=[{"message": "Not found", "details": details}])
