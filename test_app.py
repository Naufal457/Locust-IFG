from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Waktu tunggu antar permintaan (dalam detik)
    host = 'https://api-legacy-wrapper-dev.ifg-life.id'  # Host API yang akan diuji

    @task
    def post_request(self):
        headers = {
            'Content-Type': 'application/json',
            'apiKey': 'lpEYhHvAzy1MIwY3rT1XpgAjZmMm8nPZ'  # Gantilah dengan apiKey yang valid
        }
        data = {
            "config": {
                "sourceRequest": "Legacy Corporate PLINDO"
            },
            "screeningAPUPPT": {
                "name": "TESTING FRAUD1",
                "idNumber": "1207202400000001",
                "idType": "NIK",
                "dob": "1969-06-09",
                "clientNumber": "1",
                "policyNumber": "1",
                "nomorMutasiWeb": "1",
                "processInstanceIdExternal": ""
            }
        }

        try:
            response = self.client.post('/api/v1/legacy/plindo/fraud/apuppt/checking', json=data, headers=headers)

            # Periksa status kode respons
            if response.status_code != 200:
                print(f"Request failed: {response.status_code} - {response.text}")
            else:
                print(f"Request succeeded: {response.status_code} - {response.text[:100]}")  # Tampilkan 100 karakter pertama dari response
        except Exception as e:
            print(f"An error occurred: {e}")



            from locust import HttpUser, task, between

class PetstoreUser(HttpUser):
    wait_time = between(1, 5)  # Waktu tunggu antar permintaan (dalam detik)
    host = 'https://petstore.swagger.io/v2'  # Host API Petstore

    @task
    def create_pet(self):
        data = {
            "id": 123456,  # ID hewan peliharaan
            "name": "Fluffy",  # Nama hewan peliharaan
            "category": {
                "id": 1,  # ID kategori
                "name": "Dogs"  # Nama kategori
            },
            "photoUrls": ["http://example.com/photo.jpg"],  # URL foto hewan peliharaan
            "tags": [
                {
                    "id": 1,  # ID tag
                    "name": "tag1"  # Nama tag
                }
            ],
            "status": "available"  # Status hewan peliharaan
        }
        response = self.client.post('/pet', json=data)
        if response.status_code == 200:
            print(f"POST /pet succeeded: {response.status_code}")
        else:
            print(f"POST /pet failed: {response.status_code} - {response.text}")



from locust import HttpUser, task, between

class FraudCheckingUser(HttpUser):
    wait_time = between(1, 5)  # Waktu tunggu antar permintaan (dalam detik)
    host = 'https://api-automation-dev.ifg-life.id'  # Host API yang akan diuji

    @task
    def post_fraud_checking(self):
        headers = {
            'Content-Type': 'application/json',
            'apiKey': 'E97baCBt8SxmDcYNyd3KwbEA0giw8ElF'  # Gantilah dengan apiKey yang valid
        }
        data = {
            "config": {
                "sourceRequest": "FRAUD",
                "screeningApuppt": True,
                "isRiskProfile": {
                    "isRiskProfile": False,
                    "riskType": ""
                }
            },
            "screeningAPUPPT": {
                "name": "AMIRUDIN",
                "idNumber": "8120649573018465",
                "idType": "NIK",
                "dob": "1992-03-27"
            },
            "processInstanceIdExternal": "2345678213"
        }

        try:
            response = self.client.post('/v2/ao-fraud/workflow/fraud-checking', json=data, headers=headers)
            if response.status_code == 200:
                print(f"POST /v2/ao-fraud/workflow/fraud-checking succeeded: {response.status_code}")
            else:
                print(f"POST /v2/ao-fraud/workflow/fraud-checking failed: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"An error occurred: {e}")