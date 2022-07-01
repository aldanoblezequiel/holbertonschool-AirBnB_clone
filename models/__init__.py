"""Models package"""
from models.engine.file_storage import FileStorage

"""Creating modile to reload"""
storage = FileStorage()
storage.reload()
