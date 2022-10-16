import json
import requests
import time


file = open('qpc.txt', 'r')
jsonFile = open('questionJson.json', 'w')
url = 'http://localhost:7512/qpc/questions/_create'

lines = file.readlines()

i = 0
for l in lines: 
    text = l.split(':')

    
    jsonLine = {
        "question": text[0],
        "answer": text[1]
    }
    # jsonFile.write(json.dumps(jsonLine))
    response = requests.post(url, jsonLine)
    print(response)


# jsonFileRead = open('questionJson.json', 'r')

# lines2 = jsonFileRead.readlines()
# for line in lines2:
#     print((line))
