"""Set up the development API server.
"""

# Fix paths for imports for production deployment
import app


if __name__ == '__main__':
    app.app.debug = True
    app.app.logger.debug('api_debug')
    app.app.run(host='0.0.0.0', port=5000)
