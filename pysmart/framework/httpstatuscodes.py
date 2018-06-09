from enum import Enum


class StatusCodes(Enum):

    # HTTP status codes
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORISED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404

    # Custom codes
    CONNECTION_ERROR = -1
