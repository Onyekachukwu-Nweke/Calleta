#!/usr/bin/python3
import uuid
from datetime import datetime
from sqlalchemy import String, Column, Integer, DateTime
from sqlalchemy.orm import declarative_base
import models

Base = declarative_base()
time_fmt = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """this class contains the general attributes
    id
    created_at : time an instance was created
    updated_at : time an instance was updated
    """
    id = Column(String(70), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        
        if kwargs:
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.strptime(kwargs['updated_at'], time_fmt)
                if key == 'updated_at':
                    value = datetime.strptime(kwargs['created_at'], time_fmt)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary
