import json

file = open('qpc.txt', 'r')
jsonFile = open('questionJson.json', 'w')

lines = file.readlines()

for l in lines: 
    text = l.split(':')
    jsonLine = {
        "question": text[0],
        "answer": text[1]
    }
    jsonFile.write(json.dumps(jsonLine))

jsonFileRead = open('questionJson.json', 'r')

lines2 = jsonFileRead.readlines()
for line in lines2:
    print(line)
