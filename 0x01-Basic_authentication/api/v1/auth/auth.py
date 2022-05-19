#!/usr/bin/env python3
""" module docs """
from typing import List, TypeVar


class Auth():
    """ Auth class
     """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth
        docs """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for items in excluded_paths:
            if items.endswith('*'):
                if path.startswith(items[:-1]):
                    return False
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization header
        docs """
        if request is None or not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user 
        docs """
        return None
