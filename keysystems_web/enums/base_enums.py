from enum import Enum


class RequestMethod(str, Enum):
    GET = 'GET'
    POST = 'POST'


class UserRole(str, Enum):
    CLIENT = 'client'
    STAFF = 'staff'
