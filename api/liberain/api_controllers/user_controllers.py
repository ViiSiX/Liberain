from . import app, _api, db, constants,mail, utils, \
    ResourceGetNotAllowed, \
    reqparse, abort
from ..models.user_models import User
from ..models.token_model import Token
from flask_mail import Message


class RegisterUser(ResourceGetNotAllowed):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('display_name', type=str,
                            help='Display Name is required.', required=True)
        parser.add_argument('email', type=str,
                            help='Email is required.', required=True)
        parser.add_argument('password', type=str,
                            help='Password is required', required=True)

        kwargs = parser.parse_args()

        errors = {}

        if kwargs.get('display_name') is None:
            errors['display_name'] = 'Display Name is required.'

        if kwargs.get('password') is None:
            errors['password'] = 'Password is required.'
        elif not utils.is_valid_password(kwargs['password']):
            errors['password'] = 'Password is not strong enough.'

        if not utils.is_valid_format_email(kwargs.get('email')):
            errors['email'] = 'Provided email is invalid.'
        else:
            existing_user = User.query.filter_by(email=kwargs['email']).first()
            if existing_user is not None:
                errors['email'] = 'Existing email in the system.'
            else:
                try:
                    new_user = User(**kwargs)
                    db.session.add(new_user)
                    db.session.commit()

                    token = Token(
                        object_code=constants.OBJECT_CODES['User'],
                        object_id=new_user.user_id,
                        expiring_in=1440
                    )
                    db.session.add(token)
                    db.session.commit()

                    msg = Message(
                        subject="Welcome to Liberain",
                        recipients=[new_user.email],
                        body="Dear {display_name},\n\nPlease notice that you (or someone) "
                             "have just registered a new account at {base_url}.\n\n"
                             "Yet the account have to be activated to use our service. You can "
                             "activate your account by click to the following link.\n"
                             "{activate_url}\n\n"
                             "I wish you can find it meaningful using our service to store "
                             "your memory together.\n\nBest regards,\nNghia from Liberain"
                            .format(
                            base_url=app.config['LIBERAIN_FRONTEND_URL'],
                            activate_url="{0}/{1}/{2}".format(
                                app.config['LIBERAIN_FRONTEND_URL'],
                                'activate',
                                token.token
                            ),
                            display_name=new_user.display_name
                        )
                    )
                    mail.send(msg)

                except Exception as e:
                    app.logger.exception(e)
                    abort(400, message={
                        'errors': {
                            'registration': 'There is problem while trying to create new user.'
                        }
                    })

        if len(errors) > 0:
            abort(400, message={'errors': errors})
        else:
            return {'message': {'success': 'User have been successfully created!'}}


class ActivateUser(ResourceGetNotAllowed):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str,
                            help='Activate token is required.', required=True)

        kwargs = parser.parse_args()

        errors = {}

        if kwargs.get('token') is None:
            errors['token'] = 'Activate token is required.'
        else:
            token = Token.query.filter_by(
                token=kwargs['token'],
                object_code=constants.OBJECT_CODES['User'],
                state=constants.TOKEN_STATES['ACTIVE']
            ).first()

            if token is None:
                errors['token'] = 'Invalid token.'
            else:
                try:
                    token.state = constants.TOKEN_STATES['INACTIVE']
                    user = User.query.filter_by(user_id=token.object_id).first()
                    if user is None:
                        errors['activation'] = 'User not found.'
                    else:
                        user.state=constants.USER_STATES['ACTIVE']
                        db.session.commit()

                except Exception as e:
                    errors['activation'] = 'There is problem while trying to activate your user.'
                    app.logger.exception(e)


        if len(errors) > 0:
            abort(400, message={'errors': errors})
        else:
            return {'message': {'success': 'User have been activated!'}}


_api.add_resource(RegisterUser, '/user/register')
_api.add_resource(ActivateUser, '/user/activate')
