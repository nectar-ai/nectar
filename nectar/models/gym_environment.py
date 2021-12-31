from pydantic import BaseModel

class GymEnvironment(BaseModel):
    environmentName: str
    environmentPath: str