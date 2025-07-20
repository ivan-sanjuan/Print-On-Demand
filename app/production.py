import pandas as pd
import pprint
import json
from app.specs.details import get_details

trim_size = get_details()

with open('lulu_specs.json', 'w') as f:
    json.dump(trim_size,f,indent=2)
    
for entry in trim_size[:5]:
    pprint.pprint(entry)