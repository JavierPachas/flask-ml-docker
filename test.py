import requests
import json
url = "http://localhost:5005/predict"
data = {"MedInc": 3.5, 
        "HouseAge": 20, 
        "AveRooms": 5.4, 
        "AveBedrms": 1.1,
        "Population": 1200, 
        "AveOccup": 3.2, 
        "Latitude": 34.2, 
        "Longitude": -118.4}

# Convert to JSON string
input_data = json.dumps(data)
# Set the content type
headers = {"Content-Type": "application/json"}
# Make the request and display the response
resp = requests.post(url, input_data, headers=headers)
print(resp.text)

