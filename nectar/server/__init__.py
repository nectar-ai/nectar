import textwrap
import logging
import waitress

from flask import Flask, Response

app = Flask(__name__)

# Provide a health check endpoint to ensure the application is responsive
@app.route("/health")
def health():
    """
    Provide a health check endpoint to ensure the application is responsive.
    """
    return "OK", 200

@app.route("/")
def serve():
    """
    Serve the index.html for the UI.
    """
    text = textwrap.dedent(
    """
    Unable to display Nectar UI - landing page (index.html) not found.
    """
    )
    return Response(text, mimetype="text/plain")

def run_server(host, port):
    """
    Call the private method to run the Nectar server
    :param None
    :return: None
    """
    _run_server(host, port)

def _run_server(host, port):
    """
    Run the Nectar server using waitress
    :param None
    :return: None
    """
    logger = logging.getLogger("waitress")
    logger.setLevel(logging.INFO)
    waitress.serve(app, host=host, port=port)
