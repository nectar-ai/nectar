import textwrap
import uvicorn

from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import List

from nectar.server import experiment

app = FastAPI()

class GymEnvironment(BaseModel):
    environmentName: str
    environmentPath: str

class Experiment(BaseModel):
    gymEnvironment: GymEnvironment
    iterations: int
    gamma: List[float]
    lr: List[float]

# Provide a health check endpoint to ensure the application is responsive
@app.get("/health")
def health(response: Response):
    """
    Provide a health check endpoint to ensure the application is responsive.
    """
    response.status_code = status.HTTP_200_OK
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

@app.post("/experiment/")
def execute_experiment(experiment_obj: Experiment):
    experiment.execute_experiment(experiment_obj)
    return "OK"

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
    uvicorn.run(app, host=host, port=port)
