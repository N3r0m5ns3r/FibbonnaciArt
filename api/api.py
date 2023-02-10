import requests

url = "https://api.newnative.ai/stable-diffusion?prompt=futuristic spce station, 4k digital art"

response = requests.request("GET", url)
data = response.json()
print(data["image_url"])
