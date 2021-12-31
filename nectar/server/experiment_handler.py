import pika

from nectar.models import Experiment

def execute_experiment_handler(experiment: Experiment):

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="experiment.queue")

    channel.basic_publish(exchange="", routing_key="experiment.queue", body=experiment.json())