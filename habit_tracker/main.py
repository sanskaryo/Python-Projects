import requests
from datetime import datetime

# after complete go to - https://pixe.la/v1/users/sankhuz/graphs/graph2.html

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "safdtf35atfctfcdstacstfxc",
    "username": "sankhuz",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create user
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Coding Graph",
    "unit": "hrs",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": user_params["token"]
}

# Create graph
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.5"
}

# Create pixel
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
