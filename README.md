# 🌄 Wallpaper Change

Automatically refresh your Windows desktop with stunning nature images from Pexels!

## ✨ What is this?

**Wallpaper Change** is a Python script that fetches a random, high-quality nature photo from Pexels and sets it as your Windows wallpaper. Enjoy a new view every time you run it—no manual downloads, no fuss!

## 🚀 Features

- **Random Nature Images:** Picks from categories like ocean, forest, nightlights, and more.
- **Instant Wallpaper Update:** Sets your desktop wallpaper in seconds.
- **API Powered:** Uses the Pexels API for beautiful, copyright-free images.
- **Easy Setup:** Just add your API key and run!

## 🛠️ Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)
- Windows OS

## ⚡ Quickstart

1. **Clone this repo:**
    ```sh
    git clone https://github.com/yourusername/wallpaper_change.git
    cd wallpaper_change
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Get your Pexels API key:**  
   [Sign up here](https://www.pexels.com/api/) and copy your key.

4. **Create a `.env` file:**
    ```
    API_KEY=your_pexels_api_key_here
    ```

5. **Run the script:**
    ```sh
    python main.py
    ```

## 🖼️ How it works

- Picks a random nature category and page.
- Fetches images from Pexels.
- Downloads and converts the image for Windows wallpaper.
- Sets your desktop background instantly!

## 💡 Customization

Want different categories?  
Edit the `image_choices` list in `main.py` to add your favorite themes!

## ❓ FAQ

- **Does it work on Mac/Linux?**  
  No, this script is Windows-only (uses Windows API).

- **Is it safe/legal to use these images?**  
  Yes! Pexels images are free for personal use.

## 📄 License

MIT

---

> Made with Python & nature love