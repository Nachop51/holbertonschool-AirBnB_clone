#!/usr/bin/python3
""" Base model module """
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Base model class"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Representation of the class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        new_dict = {key: value for key, value in self.__dict__.items()}
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
