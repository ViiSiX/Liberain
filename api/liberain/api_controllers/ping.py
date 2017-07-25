from . import _api, \
    Resource


class Pong(Resource):
    def get(self):
        return {
            'ping': 'pong'
        }


_api.add_resource(Pong, '/ping')
