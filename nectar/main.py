from waitress import serve
from server import app

import logging

if __name__ == "__main__":
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.INFO)   
    serve(app, host='127.0.0.1', port=5000)