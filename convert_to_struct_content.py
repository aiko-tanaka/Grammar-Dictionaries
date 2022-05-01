# code i used to convert from non-struct content into struct content

import json

with open('term_bank_1.json', 'r', encoding='UTF8') as fh:
    initial_data : list = json.load(fh)

new_data = initial_data

for index, x in enumerate(initial_data):
    old_format = x[5][0]
    new_format = { "type": "structured-content", "content" : [old_format]}

    new_data[index][5][0] = new_format

with open('term_bank_new.json', 'w', encoding='UTF8') as fh:
    json.dump(new_data, fh, indent=4, ensure_ascii=False)
