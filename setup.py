import os
import json

database_list = [
    'customer.json',
    'employee.json',
    'item.json',
    'order.json'
]

database = 'database'

os.makedirs(database, exist_ok=True)

init_database = {}

for db in database_list:
    with open(os.path.join(database, db), 'w') as f:
        f.write(json.dumps(init_database, indent=4))
