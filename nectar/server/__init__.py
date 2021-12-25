import textwrap
import logging
import waitress

from flask import Flask, Response

app = Flask(__name__)

# Provide a health check endpoint to ensure the application is responsive
@app.route("/health")
def health():
    return "OK", 200

@app.route("/")
def serve():
    text = textwrap.dedent(
    """
    Unable to display Nectar UI - landing page (index.html) not found.
    """
    )
    return Response(text, mimetype="text/plain")

def _run_server():
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.INFO)   
    waitress.serve(app, host='127.0.0.1', port=5000)