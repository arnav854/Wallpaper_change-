import requests
import random
import ctypes
import os
from PIL import Image  
from dotenv import load_dotenv
load_dotenv()
 
api_key = os.getenv("API_KEY")

url = "https://api.pexels.com/v1/search"

headers = {
    "Authorization": api_key
}

image_choices = ["Ocean", "nature", "cloud", "woodlands", "forest", "grassland", "rainfall", "nightlights"]

def fetch_pexel_img_data():
    params = {
        "query": random.choice(image_choices),
        "per_page": 5,
        "page": random.randint(1, 15)
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if "photos" not in data or len(data["photos"]) == 0:
            print("No images found.")
            return

        photo = random.choice(data["photos"])
        image_url = photo["src"]["original"]

        img_response = requests.get(image_url)
        with open("wallpaper.jpg", "wb") as file:
            file.write(img_response.content)

        img = Image.open("wallpaper.jpg")
        img.save("wallpaper.bmp")

        bmp_path = os.path.abspath("wallpaper.bmp")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, bmp_path, 3)

        print("✅ Wallpaper set successfully!")

    except Exception as e:
        print("❌ Error occurred:", e)

# Run
def main():
    fetch_pexel_img_data()

if __name__ == "__main__":
    main()
