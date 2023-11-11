#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class inherits from BaseModel
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    def to_dict(self):
        """
        Return dictionary representation of User class.
        """
        user_dict = super().to_dict()
        user_dict['email'] = self.email
        user_dict['password'] = self.password
        user_dict['first_name'] = self.first_name
        user_dict['last_name'] = self.last_name
        return user_dict
