#!/usr/bin/env python3
""" module
docs """
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ auten basica
    def """

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """ methodos
        autori """
        if authorization_header is None or \
                not isinstance(authorization_header, str) or \
                not authorization_header.startswith("Basic "):
            return None
        ba = authorization_header.split(' ')
        return ba[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ mmotos if """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None
        try:
            baseEncode = base64_authorization_header.encode('utf-8')
            return b64decode(baseEncode).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str ) -> (str, str):
        """ decode met """
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str) or \
                ':' not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ credentials use """
        if user_email is None or not isinstance(user_email, str) or \
                user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        try:
            header = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(header)
            decodeValue = self.decode_base64_authorization_header(base64Header)
            credentials = self.extract_user_credentials(decodeValue)
            user = self.user_object_from_credentials(credentials[0],
                                                     credentials[1])
            return user
        except Exception:
            return None
