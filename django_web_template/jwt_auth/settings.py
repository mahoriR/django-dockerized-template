################################################
# https://github.com/GetBlimp/django-rest-framework-jwt/tree/master/rest_framework_jwt
################################################

import datetime

from django.conf import settings
from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'JWT_AUTH', None)

DEFAULTS = {
    'JWT_ENCODE_HANDLER': 'jwt_auth.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER': 'jwt_auth.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER': 'jwt_auth.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER': 'jwt_auth.utils.jwt_get_user_id_from_payload_handler',

    'JWT_PRIVATE_KEY': None,

    'JWT_PUBLIC_KEY': None,

    'JWT_RESPONSE_PAYLOAD_HANDLER': 'jwt_auth.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': settings.SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': 'jwt_auth.utils.jwt_get_secret_key_for_user',
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,
    'JWT_INITIAL_EXPIRATION_DELTA': datetime.timedelta(hours=2),
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = (
    'JWT_ENCODE_HANDLER',
    'JWT_DECODE_HANDLER',
    'JWT_PAYLOAD_HANDLER',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER',
    'JWT_RESPONSE_PAYLOAD_HANDLER',
    'JWT_GET_USER_SECRET_KEY',
)

api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
