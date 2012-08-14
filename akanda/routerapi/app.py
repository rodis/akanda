"""Set up the API server application instance
"""

import flask

from akanda.routerapi import v1

app = flask.Flask(__name__)
app.register_blueprint(v1.base.base)
app.register_blueprint(v1.system.system)
app.register_blueprint(v1.firewall.firewall)


@app.before_request
def attach_config():
    '''
        Attach any configuration before instantiating API
    '''
    pass
