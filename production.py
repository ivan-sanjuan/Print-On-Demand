import pandas as pd
import pprint
import json

trim_size = get_trimSize()

with open('lulu_specs.json', 'w') as f:
    json.dump(trim_size,f,indent=2)
    
for entry in trim_size[:5]:
    pprint.pprint(entry)