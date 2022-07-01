#!/usr/bin/python3
"""
    City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class - inherit BaseModel"""

    state_id = ""
    name = ""
