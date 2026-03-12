import pandas as pd
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class GoogleMapsProfessionalScraper:
    def __init__(self):
        options = Options()
        # Aktifkan headless jika ingin berjalan di background
        # options.add_argument("--headless") 
        options.add_argument("--window-size=1920,1080")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.all_results = []

    def scrape_maps(self, category, city):
        """Mencari data bisnis di Google Maps dengan sistem scrolling"""
        search_query = f"{category} in {city}, Spain"
        print(f"[*] Searching: {search_query}")
        
        # URL pencarian langsung Google Maps
        url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"
        self.driver.get(url)
        
        try:
            # Tunggu hingga sidebar hasil pencarian muncul
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="feed"]')))
            
            # Identifikasi panel samping untuk di-scroll
            side_panel = self.driver.find_element(By.XPATH, '//div[@role="feed"]')
            
            # Sistem Scrolling untuk memuat lebih banyak hasil
            last_height = self.driver.execute_script("return arguments[0].scrollHeight", side_panel)
            for _ in range(5):  # Sesuaikan angka range untuk lebih banyak data
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', side_panel)
                time.sleep(2)
                new_height = self.driver.execute_script("return arguments[0].scrollHeight", side_panel)
                if new_height == last_height:
                    break
                last_height = new_height

            # Ambil semua elemen bisnis (biasanya class hfpxzc adalah link utama)
            items = self.driver.find_elements(By.CLASS_NAME, "hfpxzc")
            
            for item in items:
                try:
                    name = item.get_attribute("aria-label")
                    # Simpan data dasar
                    if name and name not in [res['Name'] for res in self.all_results]:
                        self.all_results.append({
                            "Name": name,
                            "Category/Query": category.capitalize(),
                            "City": city.capitalize(),
                            "Source": "Google Maps",
                            "Search Context": search_query
                        })
                except:
                    continue
            
            print(f"[+] Found {len(items)} potential leads in {city}.")

        except Exception as e:
            print(f"[!] No results or timeout for {search_query}.")

    def export_data(self, filename="GoogleMaps_Spain_Leads"):
        if not self.all_results:
            print("[!] Database empty.")
            return

        df = pd.DataFrame(self.all_results)
        # Menghapus duplikat berdasarkan Nama
        df = df.drop_duplicates(subset=['Name'])
        
        # Export ke Excel
        output_file = f"{filename}.xlsx"
        df.to_excel(output_file, index=False)
        print(f"\n{'='*30}\nDATABASE SAVED: {output_file}\nTotal Records: {len(df)}\n{'='*30}")

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = GoogleMapsProfessionalScraper()
    
    # Query Dinamis: Semua profesi (Fokus pada kata kunci Italian-Speaking)
    professions = [
        "Italian speaking lawyer", "Italian doctor", "Real estate agency", 
        "Translator Italian Spanish", "Italian Restaurant", "Consultant",
        "Accountant", "Notary", "Insurance agency", "Architect"
    ]
    
    # Query Dinamis: Semua kota besar di Spanyol
    cities = [
        "Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", 
        "Malaga", "Murcia", "Palma", "Bilbao", "Alicante"
    ]

    try:
        for city in cities:
            for prof in professions:
                bot.scrape_maps(prof, city)
                # Jeda antar pencarian agar aman
                time.sleep(random.uniform(3, 7))

        bot.export_data("Master_GoogleMaps_Spain_Directory")

    finally:
        bot.quit()