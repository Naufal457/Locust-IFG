from locust import HttpUser, task, between
import json

class FraudCheckingUser(HttpUser):
    wait_time = between(1, 2)  # Waktu tunggu antara request dalam detik

    @task
    def fraud_checking(self):
        headers = {
            'apiKey': 'E97baCBt8SxmDcYNyd3KwbEA0giw8ElF',
            'Content-Type': 'application/json',
        }

        payload = {
            "config": {
                "sourceRequest": "Legacy Retail",
                "isRiskProfile": {
                    "isRiskProfile": True,
                    "riskType": "Retail"
                },
                "screeningApuppt": True
            },
            "screeningAPUPPT": {
                "name": "Timur Zhanibekol",
                "idNumber": "1050176605823067",
                "idType": "NIK",
                "dob": "1989-09-03"
            },
            "riskProfile": {
                "retailRiskProfile": {
                    "policyHolderName": "Timur Zhanibekol",
                    "alias": "Timur Zhanibekol",
                    "beneficiaryName": "Timur Zhanibekol",
                    "policyHolderIdNumber": "1050176605823067",
                    "policyHolderAddress": "JL. Kebun Mangga V",
                    "policyHolderPhone": "088176282791",
                    "policyHolderDateOfBirth": "1989-09-03",
                    "policyHolderPlaceOfBirth": "Bandung",
                    "beneficiaryDateOfBirth": "1989-09-03",
                    "nationality": "INDONESIA",
                    "policyHolderJob": "wakil presiden",
                    "policyHolderJobAddress": "JL. Pasir Kuning V",
                    "policyHolderJobPhone": "088176282791",
                    "policyHolderGender": "Laki-Laki",
                    "policyHolderMaritalStatus": "Lajang",
                    "averageEarnings": "Rp. 10.000.000",
                    "policyCoverageArea": "31.72",
                    "typeOfInsurance": "unit link",
                    "totalPremium": "200000000",
                    "paymentMethod": "ATM",
                    "insuranceStartDate": "2014-01-09",
                    "insuranceObjective": "Pengalihan Resiko",
                    "dataUpdated": "2014-10-13",
                    "insuranceProduct": "AnuitasPRIMA"
                }
            }
        }

        # URL lengkap API
        url = 'https://api-automation-dev.ifg-life.id/v2/ao-fraud/workflow/fraud-checking'

        response = self.client.post(url, headers=headers, data=json.dumps(payload))

        # Menampilkan waktu respons
        print(f"Response time: {response.elapsed.total_seconds()} seconds")

        # Memastikan status code yang benar (201 Created)
        assert response.status_code == 201
