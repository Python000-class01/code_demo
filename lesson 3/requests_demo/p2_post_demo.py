import requests
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r.json()


import json
python_string = {
   'name' : 'value',
   'name2' : 'value2',
   'name3' : 'value3'
}
json_string = json.dumps(python_string)
python_string2 = json.loads(json_string)