#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_pat = len(path)
        if l_pat == 0:
            return True

        slas_path = True if path[l_pat - 1] == '/' else False

        tmp_pat = path
        if not slas_path:
            tmp_pat += '/'

        for exc in excluded_paths:
            l_ex = len(exc)
            if l_ex == 0:
                continue

            if exc[l_ex - 1] != '*':
                if tmp_pat == exc:
                    return False
            else:
                if exc[:-1] == path[:l_ex - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles the authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validate the current user"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""

        if request is None:
            return None

        SESSION_NAME = getenv("SESSION_NAME")

        if SESSION_NAME is None:
            return None

        sesion_id = request.cookies.get(SESSION_NAME)

        return sesion_id
