#!/usr/bin/python3
"""

Module executed when the models package is imported

"""

from models.engine.file_storage import FileStorage

"""
Retrives the storage instance

"""

storage = FileStorage()
storage.reload()
