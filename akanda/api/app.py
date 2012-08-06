"""Set up the API server application instance
"""

# Fix paths for imports for production deployment
import flask

import v1


app = flask.Flask('api')
app.register_blueprint(v1.blueprint, url_prefix='/v1')


@app.before_request
def attach_config():
    #Use for attaching config prior to starting
    pass


@app.route('/')
def welcome():
    return 'Welcome to Akanda'