import json

def write(json_per_line, filename):
    with open(filename,'w') as outf:
        for record in json_per_line:
            outf.write(json.dumps(record)+'\n')
