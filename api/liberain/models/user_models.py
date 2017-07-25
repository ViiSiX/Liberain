"""Docstring for User Model."""

from . import app, utils, constants
from . import _db
from sys import version_info
from jose import jwt
import datetime


class User(_db.Model):
    """
    Docstring for User Model class.

    The User class represent for the User table
    contain a user's information.
    """

    user_id = _db.Column('id', _db.Integer,
                         primary_key=True,
                         autoincrement=True)
    email = _db.Column('emailAddress', _db.String(255),
                       index=True,
                       unique=True,
                       nullable=False)
    display_name = _db.Column('displayName', _db.String(255),
                           nullable=False)
    _password = _db.Column('passwordHashed', _db.String(255),
                           nullable=False)
    created_on = _db.Column('createdOn', _db.DateTime,
                            nullable=False,
                            default=datetime.datetime.now)
    updated_on = _db.Column('updatedOn', _db.DateTime,
                            nullable=False,
                            default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    state = _db.Column('state', _db.SmallInteger,
                       nullable=False,
                       default=constants.USER_STATES['UNACTIVATED'])
    version = _db.Column(_db.SmallInteger,
                         nullable=False,
                         default=constants.MODELS_VERSION[
                             constants.OBJECT_CODES['User']
                         ])

    def get_id(self):
        """Get the user id in unicode string. This is the standard for later
        changes that ID would always be a string for upper layers."""

        if self.user_id is None:
            return ''
        if version_info >= (3, 0):
            return str(self.user_id)
        return unicode(self.user_id)

    @property
    def password(self):
        """Transparent and provide the value of _password (hashed) attribute
        to consumer."""

        return self._password

    @password.setter
    def password(self, password):
        """
        Hashing the input and set hashed string to the _password attribute.

        :param password:
        :return:
        """
        self._password = utils.hash_password(password)

    def verify_password(self, password):
        """
        Verify if the provided password is matching with the current user's
        hashed password.

        :param password:
        :return:
        """
        return utils.verify_password(password, self.password)

    def generate_auth_token(self, expiration=3600):
        """
        Generate a JSON Web Token using for authentication after the login.

        :param expiration:
        :return:
        """

        return jwt.encode(
            {id: self.user_id},
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )

    def __repr__(self):
        """Define how to present one entity of this class as a string."""

        return '<Liberain.User {email} - Id {id}>'.format(
            email = self.email,
            id = self.user_id
        )
