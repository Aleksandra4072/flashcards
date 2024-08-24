from fastapi import HTTPException


class Error401(HTTPException):
    def __init__(self, detail: str):
        super().__init__(401, detail=detail)


class Error400(HTTPException):
    def __init__(self, detail: str):
        super().__init__(400, detail=detail)


class Error403(HTTPException):
    def __init__(self, detail: str):
        super().__init__(403, detail=detail)


class Error404(HTTPException):
    def __init__(self, detail: str):
        super().__init__(403, detail=detail)
