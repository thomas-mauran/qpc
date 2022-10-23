import json
import requests
import time


file = open('qpc.txt', 'r')
jsonFile = open('questionJson.json', 'w')
url = 'http://localhost:7512/qpc/questions/_create'

lines = file.readlines()

i = 1
for l in lines: 
    text = l.split(':')

    
    jsonLine = {
        "id": i,
        "question": text[1],
        "answer": text[0]
    }
    # jsonFile.write(json.dumps(jsonLine))
    response = requests.post(url, jsonLine)
    i+= 1


# jsonFileRead = open('questionJson.json', 'r')

# lines2 = jsonFileRead.readlines()
# for line in lines2:
#     print((line))
