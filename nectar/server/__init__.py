import textwrap
import logging
import uvicorn

from fastapi import FastAPI, Response, status

app = FastAPI()

# Provide a health check endpoint to ensure the application is responsive
@app.get("/health")
def health(response: Response):
    """
    Provide a health check endpoint to ensure the application is responsive.
    """
    response.status_code = status.HTTP_201_CREATED
    return "OK"

@app.get("/")
def serve():
    """
    Serve the index.html for the UI.
    """
    text = textwrap.dedent(
    """
    Unable to display Nectar UI - landing page (index.html) not found.
    """
    )
    return Response(content=text, media_type="text/plain")

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
    uvicorn.run(app, host=host, port=port)
