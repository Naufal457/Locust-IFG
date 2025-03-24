from locust import HttpUser, task, between
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime

# Load .env file untuk mengambil API key
load_dotenv()
API_KEY = os.getenv("API_KEY")  # Pastikan API key ada di file .env

# Path ke file CSV
data_file_path = r"C:\LocustIFG\Generated_Data_for_100_Records.csv"  # Sesuaikan dengan lokasi file Anda
df = pd.read_csv(data_file_path)  # Membaca file CSV

class APITestUser(HttpUser):
    wait_time = between(1, 3)  # Waktu tunggu antar request (1-3 detik)

    @task
    def fraud_checking(self):
        # Ambil data secara acak dari CSV
        record = df.sample(1).iloc[0]

        # Ubah format DOB dari dd/mm/yyyy ke yyyy-mm-dd
        dob = datetime.strptime(record["Date of Birth"], "%d/%m/%Y").strftime("%Y-%m-%d")

        # Buat payload berdasarkan data dari CSV
        payload = {
            "config": {
                "sourceRequest": "Legacy Corporate",
                "screeningApuppt": True
            },
            "screeningAPUPPT": {
                "name": record["Name"],       # Ambil Name dari CSV
                "idNumber": record["NPWP"],   # Ambil NPWP dari CSV
                "idType": "NPWP",             # Statis sesuai contoh
                "dob": dob                    # DOB dengan format yyyy-mm-dd
            }
        }

        # Kirim POST request ke endpoint API
        self.client.post(
            url="https://api-automation-uat.ifg-life.id/v2/ao-fraud/workflow/fraud-checking",  # URL endpoint
            headers={
                "Content-Type": "application/json",
                "apiKey": API_KEY  # Menggunakan API key dari file .env
            },
            json=payload
        )
