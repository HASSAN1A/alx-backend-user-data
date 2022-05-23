#!/usr/bin/env python3
""" Module of Session Authentication
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session Authentication Class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""

        if user_id is None or not isinstance(user_id, str):
            return None

        sesion_id = str(uuid.uuid4())

        self.user_id_by_session_id[sesion_id] = user_id

        return sesion_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""

        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User 
        instance based on a cookie value"""

        sesion_id = self.session_cookie(request)

        if sesion_id is None:
            return None

        usr_id = self.user_id_for_session_id(sesion_id)

        return User.get(usr_id)

    def destroy_session(self, request=None):
        """Deletes de user 
        session / logout"""

        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass

        return True
