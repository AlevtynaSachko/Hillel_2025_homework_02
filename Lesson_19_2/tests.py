import requests

BASE = "http://127.0.0.1:8080"

# 1. Завантаження зображення
with open("mars_photo1.jpg", "rb") as f:
    r = requests.post(f"{BASE}/upload", files={"image": f})
print("UPLOAD:", r.status_code, r.json())

# Запам'ятати ім'я файлу
filename = r.json()["image_url"].split("/")[-1]

# 2. Отримати JSON з URL
r = requests.get(f"{BASE}/image/{filename}")
print("GET JSON:", r.status_code, r.json())

# 3. Завантажити саме зображення
r = requests.get(f"{BASE}/uploads/{filename}")
print("GET IMAGE:", r.status_code, "bytes:", len(r.content))

# 4. Видалити файл
r = requests.delete(f"{BASE}/delete/{filename}")
print("DELETE:", r.status_code, r.json())