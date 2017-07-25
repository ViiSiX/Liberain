"""In here define the constants of Liberain."""


# Object's Code
# These codes will be used to identified Models and other object
# through through the system.
OBJECT_CODES = {
    'User': 0,
    'Token': 99
}
OBJECT_CODES_REVERSE = {
    0: 'User',
    99: 'Token'
}


# Models' Version
MODELS_VERSION = {
    OBJECT_CODES['User']: 1,
    OBJECT_CODES['Token']: 1
}


# User's state
USER_STATES = {
    'UNACTIVATED': 0,
    'ACTIVE': 1
}


# Token's state
TOKEN_STATES = {
    'ACTIVE': 0,
    'INACTIVE': 1
}


# Error messages
ERROR_MESSAGES = {
    'GET_NOT_ALLOWED': 'GET method is not allowed in this API.'
}
