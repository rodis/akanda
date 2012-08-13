"""Set up Development instance
"""
from akanda.routerapi.app import app


def __main__():
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    __main__()
