import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
from ultralytics import YOLO
import pandas as pd
import time

# Cache model loading
@st.cache_resource
def load_model():
    # Replace 'schiebelehre_model.pt' with the path to your trained YOLO model
    return YOLO('schiebelehre_model.pt')

model = load_model()

st.title("Schiebelehre Checker (Ricardo)")

search_term = st.text_input("Suchbegriff", value="schiebelehre")
max_items = st.slider("Max Inserate", 1, 50, 25)
if st.button("Start Analyse"):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # Build Ricardo search URL
    search_url = f"https://www.ricardo.ch/de/s/{search_term}?sort=publicationdate_desc"
    driver.get(search_url)
    time.sleep(3)
    items = driver.find_elements("css selector", "a.card__link")
    links = [item.get_attribute("href") for item in items][:max_items]

    results = []
    for link in links:
        driver.get(link)
        time.sleep(2)
        # Get main image URL
        img_el = driver.find_element("css selector", "img.ListingMediaCarousel_media__image__1D-dM")
        img_src = img_el.get_attribute("src")
        img_data = requests.get(img_src).content
        with open("temp.jpg", "wb") as f:
            f.write(img_data)

        # Run detection
        res = model("temp.jpg")
        detected = any(b.cls == model.names.index("schiebelehre") for b in res[0].boxes)
        score = max((b.conf for b in res[0].boxes if b.cls == model.names.index("schiebelehre")), default=0)

        # Extract price, condition, shipping, description
        price = driver.find_element("css selector", "[data-testid='ad-price']").text
        try:
            condition = driver.find_element("css selector", "[data-testid='ad-condition']").text
        except:
            condition = "nicht angegeben"
        desc = driver.find_element("css selector", "[data-testid='ad-description']").text
        # Shipping info in description
        shipping = "Ja" if "Versand" in desc else "Nein"

        results.append({
            "Link": link,
            "Treffer": "✅" if detected else "❌",
            "Score": f"{score:.2f}",
            "Preis": price,
            "Zustand": condition,
            "Versand": shipping,
            "Beschreibung": desc[:50] + "..."
        })

    df = pd.DataFrame(results)
    st.table(df)
    driver.quit()
