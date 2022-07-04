#!/usr/bin/python3
import sys
import sys.path
from models.base_model import BaseModel

sys.path.insert(0, './models')
model = BaseModel()
model.name = "My First Model"
model.my_number = 89
print(model)
model.save()
print(model)
model_json = model.to_dict()
print(model_json)
print("JSON of my_model:")
for key in model_json.keys():
    print("\t{}: ({}) - {}".format(key,
                                   type(model_json[key]), model_json[key]))
