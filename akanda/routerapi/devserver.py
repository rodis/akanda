import flask
from akanda.routerapi import v1

api = flask.Flask(__name__)
api.register_blueprint(v1.blueprint, url_prefix='/v1')


@api.before_request
def attach_config():
    pass


def __main__():
    api.debug = True
    #api.logger.debug('api_debug')
    api.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    __main__()
