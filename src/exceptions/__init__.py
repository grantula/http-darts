from fastapi import HTTPException

class HTTPNotImplementedException(HTTPException):
    _status_code = 405
    _detail = "This method has not been implemented yet"
    def __init__(self):
        self.status_code = self._status_code
        self.detail = self._detail