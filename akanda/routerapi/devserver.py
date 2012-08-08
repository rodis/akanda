from akanda.routerapi.v1 import app


def __main__():
    app.debug = True
    app.logger.debug('api_debug')
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    __main__()
