import requests

def get_mars_photos(sol=1000, camera="fhaz", api_key="DEMO_KEY", limit=2):
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {"sol": sol, "camera": camera, "api_key": api_key}
    response = requests.get(url, params=params)
    data = response.json()
    photos = data["photos"]
    return [photo["img_src"] for photo in photos[:limit]]

def test_get_mars_photos():
    urls = get_mars_photos(limit=2)
    assert isinstance(urls, list) # результат має бути списком
    assert len(urls) == 2 # повинно бути 2 фото
    for url in urls:
        assert url.startswith("http") # перевірка, що посилання справжнє