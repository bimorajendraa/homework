import requests
import json

url = 'https://www.affirmations.dev'
response =  requests.get(url)
if response.status_code==200:
    array = json.loads(response.text)
    print(array)

urls="https://api.adviceslip.com/advice"
responses =  requests.get(urls)
if responses.status_code==200:
    result = {}
    array=[]
    for p in range(3):
        array[p] = json.loads(responses.text)
    for i in range(3):
        result = array["slip"]["advice"]

    print(result)
