from typing import List
import pika

from pydantic import BaseModel

class GymEnvironment(BaseModel):
    environmentName: str
    environmentPath: str

class Experiment(BaseModel):
    gymEnvironment: GymEnvironment
    iterations: int
    gamma: List[float]
    lr: List[float]

def execute_experiment(experiment: Experiment):

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="experiment.queue")

    channel.basic_publish(exchange="", routing_key="experiment.queue", body=experiment.json())