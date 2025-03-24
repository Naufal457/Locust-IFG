from locust import HttpUser, TaskSet, task, between
import json
import random

class APITaskSet(TaskSet):
    
    def on_start(self):
        # Memuat API key dan sourceRequest dari file terpisah
        with open("variables.json") as f:
            self.variables = json.load(f)

    @task
    def send_request(self):
        # Generate client number dengan tepat 10 digit
        client_number = f"{random.randint(1000000000, 9999999999)}"

        # Data JSON yang akan dikirim dalam request
        payload = {
            "config": {
                "sourceRequest": "Legacy Corporate PLINDO"  # Tetap pada nilai yang diminta
            },
            "screeningAPUPPT": {
                "name": "BOBYSIFULYNA",
                "idNumber": "3671075607800002",
                "idType": "NIK",
                "dob": "1982-01-08",
                "clientNumber": client_number,
                "policyNumber": "0000001010",
                "nomorMutasiWeb": "0000001010",
                "processInstanceIdExternal": None
            }
        }

        headers = {
            "apiKey": self.variables["apiKey"],
            "Content-Type": "application/json"
        }

        # Mengirim request POST ke API
        self.client.post("/api/v1/legacy/plindo/fraud/apuppt/checking", 
                         headers=headers, 
                         json=payload)

class APIUser(HttpUser):
    tasks = [APITaskSet]
    wait_time = between(1, 3)  # Waktu tunggu antara request (1-3 detik)
    host = "https://api-legacy-wrapper-dev.ifg-life.id"  # Base URL API


#locust -f LocustTest.py
  #      @task
 #        def loginV2(self):
   #         self.client.post(
      #               url="/api/auth/v2/login",
   #                  headers={"x-signature": signature},
      #               json= {
      #                      "username": "CU_LKL_S",
      #                       "password": "Nsel@1234",
      #                       "branchCode": "LUKOIL"
       #                  }
       #          )
#locust -f LocustTest.py
#http://gym-master.apps.ocp-new-dev.bri.co.id
#Invoice Smart Billing Management 
#    self.client.post(
#                         url="http://gym-master.apps.ocp-new-dev.bri.co.id/api/create-briva-upload/billing-detail",
#                         headers={"authorization": "Bearer "+ token},
#                         json= {
#                             "body": {"billingDetailId": "70566"}
#                         }
#                 )