import requests

# Making a POST request
r = requests.get('http://localhost:8000/api/user', headers={'Authorization':'Token 088767aa335b16024ff726ccd661043625dc6cc8'})

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.json())
