import json
import random
import time
import os
from datetime import datetime

# Folder tempat menyimpan file JSON
output_folder = "stream_data"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Data simulasi
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset", "Webcam"]
cities = ["Jakarta", "Bandung", "Surabaya", "Medan", "Yogyakarta"]

counter = 1

# Loop utama untuk generate data secara terus-menerus
while True:
    
    # Membuat dictionary data transaksi secara acak
    transaction = {
        "user_id": random.randint(100, 200),
        "product": random.choice(products),
        "price": random.randint(50, 2000),
        "city": random.choice(cities),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Membuat nama file dan path lengkapnya
    filename = f"transaction_{counter}.json"
    filepath = os.path.join(output_folder, filename)
    
    # Menulis data ke file JSON
    with open(filepath, "w") as f:
        json.dump(transaction, f)
        
    print("Generated:", transaction)
    
    # Menambah counter untuk nama file berikutnya
    counter += 1
    
    # Menunggu selama 3 detik sebelum generate data baru
    time.sleep(3)