from passlib.hash import argon2
import re
import uuid
import datetime


def hash_password(raw_password):
    """

    :param raw_password: Password in clear text.
    :return: Encrypted password.
    """

    return argon2.hash(raw_password)


def generate_token():
    """Generate a random hex token using uuid module."""

    return uuid.uuid4().hex


def get_time_delta_in_minutes(t1, t2):
    """Calculate and get the difference between two timestamp.

    :type t1: datetime.datetime
    :type t2: datetime.datetime
    """

    dt_delta = t2 - t1
    return dt_delta.seconds/60


def add_minutes_to_datetime(t, n):
    """Add n minutes to the timestamp t.

    :param t: timestamp that will be worked on.
    :type t: datetime.datetime
    :param n: number of minutes that will be add to timestamp t.
    :type n: int
    """

    return t + datetime.timedelta(minutes=n)


def verify_password(raw_password, hashed_password):
    """

    :param raw_password: Password in clear text.
    :param hashed_password: Hashed password from database.
    :return: True/False for matching result.
    """

    return argon2.verify(raw_password, hashed_password)


def is_valid_format_email(email):
    """Return if a given string is email or not."""

    try:
        return bool(
            re.search(r'^.*?@([\w\-]+\.)+[\w\-]+$', email, flags=re.IGNORECASE)
        )
    except TypeError:
        raise TypeError('Email should be string, not %s' % type(email))


def is_valid_password(password):
    """
    Return if a password is valid or not.

    A valid password should have its length greater than 8, contain at least one
    digit, one uppercase letter, one lowercase letter and one special character.
    """

    try:
        is_valid = True
        is_valid &= len(password) >= 8
        is_valid &= re.search(r'\d', password) is not None
        is_valid &= re.search(r'[A-Z]', password) is not None
        is_valid &= re.search(r'[a-z]', password) is not None
        is_valid &= re.search(r'\W?_', password) is not None
        return is_valid
    except TypeError:
        raise TypeError('Password should be string, not %s' % type(password))
