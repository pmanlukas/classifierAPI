import pickle
import json
import pandas

with open('specs_eval_api.pkl', 'rb') as handle:
    specs = pickle.load(handle)

print(specs.keys())

