#!/usr/bin/python3
"""
initialize the models package
"""

from models.engine.Db_storage import DBStorage

storage = DBStorage()
storage.reload()