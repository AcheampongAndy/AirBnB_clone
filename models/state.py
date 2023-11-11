#!/usr/bin/python3

from models.base_model import BaseModel

class State(BaseModel):
    """
    Initializing the class

    Parameters:
    name: string - empty string
    """
    name: str = ""

    def to_dict(self):
        """
        Return dictionary representation of State class.
        """
        state_dict = super().to_dict()
        state_dict['name'] = self.name
        return state_dict