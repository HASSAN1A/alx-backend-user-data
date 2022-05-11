#!/usr/bin/env python3
""" password encryption """
import bcrypt


def hash_password(password: str) -> bytes:
    """ expects a string argument name password and returns a salted,
        hash password, which is a string of bytes. """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ expects 2 arguments and returns a boolean value."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
