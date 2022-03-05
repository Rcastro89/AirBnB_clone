#!/usr/bin/python3
"""class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """class that inherits from BaseModel"""
    state_id = str()
    name = str()

    def __init__(self, *args, **kwargs):
        """Method Init"""
        super().__init__(*args, **kwargs)
