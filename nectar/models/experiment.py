from pydantic import BaseModel
from typing import List

from .gym_environment import GymEnvironment

class Experiment(BaseModel):
    algorithms: List[str]
    gymEnvironment: GymEnvironment
    iterations: int
    gamma: List[float]
    lr: List[float]