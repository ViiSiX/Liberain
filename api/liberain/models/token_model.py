"""Docstring for Token Model."""

from . import constants, utils
from . import _db
import datetime


class Token(_db.Model):
    """Docstring for Token Model class.

    This class represent for Token table in which storing the
    token which is used by the application, for example: activation
    token for new user.
    """

    token_id = _db.Column('id', _db.Integer,
                          primary_key=True,
                          autoincrement=True)
    token = _db.Column('token', _db.VARCHAR(40),
                       index=True,
                       nullable=False,
                       default=utils.generate_token)
    created_on = _db.Column('createdOn', _db.DateTime,
                            nullable=False,
                            default=datetime.datetime.now)
    _expired_on = _db.Column('expiredOn', _db.DateTime,
                             nullable=True)
    object_code = _db.Column('objectCode', _db.SmallInteger,
                             nullable=False)
    object_id = _db.Column('objectId', _db.Integer,
                           nullable=False,
                           default=0)
    state = _db.Column('state', _db.SmallInteger,
                       nullable=False,
                       default=constants.TOKEN_STATES['ACTIVE'])
    version = _db.Column(_db.SmallInteger,
                         nullable=False,
                         default=constants.MODELS_VERSION[
                             constants.OBJECT_CODES['Token']
                         ])

    @property
    def expiring_in(self):
        if self._expired_on is None:
            return 0
        else:
            return utils.get_time_delta_in_minutes(
                self.created_on,
                self._expired_on
            )

    @expiring_in.setter
    def expiring_in(self, keep_alive_in_minutes=1440):
        if keep_alive_in_minutes == 0:
            self._expired_on = None
        else:
            if self.created_on is None:
                self.created_on = datetime.datetime.now()

            self._expired_on = utils.add_minutes_to_datetime(
                self.created_on,
                keep_alive_in_minutes
            )

    def __repr__(self):
        """Define how to present one entity of this class as a string."""

        return '<Liberain.Token {token_left}xxx{token_right} - ' \
               '<{object_name} {object_id}>>'\
            .format(
                token_left=self.token[:4],
                token_right=self.token[-4:],
                object_name=constants.OBJECT_CODES_REVERSE[self.object_code],
                object_id=self.object_id
            )
