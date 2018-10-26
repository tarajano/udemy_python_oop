

import json

dct = {'a': [1,2,3,4], 'b': 'Manu made me store it.'}

with open('json.json', 'w') as jf:
    json.dump(dct, jf)

with open('json.json', 'r') as jf:
    new_json = json.load(jf)

print(str(new_json))

