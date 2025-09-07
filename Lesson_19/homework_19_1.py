import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
params = {
    "sol": 1000,
    "camera": "fhaz",
    "api_key": "DEMO_KEY" # або свій ключ
}

response = requests.get(url, params=params)
data = response.json()

photos = data["photos"]

for i, photo in enumerate(photos[:2], start=1):
    img_url = photo["img_src"]
    img_data = requests.get(img_url).content
    with open(f"mars_photo{i}.jpg", "wb") as f:
        f.write(img_data)
    print(f"Збережено mars_photo{i}.jpg")