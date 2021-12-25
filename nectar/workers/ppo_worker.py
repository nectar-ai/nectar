import pika
import json
import ray

from ray import tune
from ray.tune import register_env, Callback

import importlib.util

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='experiment.queue')
channel.queue_declare(queue='experiment.results.queue')

class PPOCallback(Callback):
    def on_trial_result(self, iteration, trials, trial, result, **info):

        data = json.dumps({
            "trialId": result['trial_id'],
            "date": result['date'],
            "algorithm": 'PPO',
            "environmentName": result['config']['env'],
            "config": {
                "gamma": result['config']['gamma'],
                "lr": result['config']['lr'],
                "evaluationNumEpisodes": result['config']['evaluation_num_episodes']
            },
            "results": {
                "episodeRewardMax": result['episode_reward_max'],
                "episodeRewardMean": result['episode_reward_mean'],
                "episodeRewardMin": result['episode_reward_min'],
                "episodeLengthMean": result['episode_len_mean'],
                "timestepsTotal": result['agent_timesteps_total'],
                "totalTimeSeconds": result['time_total_s']
            }
        })

        # channel.basic_publish(
        #     exchange='',
        #     routing_key='experiment.results.queue',
        #     body=data
        # )

def train_ppo(environment_name, environment_path, iterations, gamma, lr):
    
    ray.init()

    spec=importlib.util.spec_from_file_location(environment_name, environment_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    register_env(environment_name, module.Example_v0)
    tune.run(
        ["PPO", "DQN"],
        stop = {
            "training_iteration": iterations,
        },
        config={
            "env": environment_name,
            "num_workers": 3,
            "gamma" : tune.grid_search(gamma),
            "lr": tune.grid_search(lr),
            "framework": "torch"
        },
        callbacks=[PPOCallback()]
    )

    ray.shutdown()

def execute_experiments(ch, method, properties, body):

    ch.basic_ack(delivery_tag=method.delivery_tag)
    
    message = json.loads(body.decode())

    environment_name = message['gymEnvironment']['environmentName']
    environment_path = message['gymEnvironment']['environmentPath']
    iterations = message['iterations']
    gamma = message['gamma']
    lr = message['lr']

    print(" [x] Received %r" % body.decode())

    train_ppo(environment_name, environment_path, iterations, gamma, lr)
    print(" [x] Done")


channel.basic_consume(
    queue='experiment.queue',
    on_message_callback=execute_experiments
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()



