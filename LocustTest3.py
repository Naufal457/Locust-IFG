from locust import HttpUser, task, between

class ApiPerformanceTest(HttpUser):
    wait_time = between(1, 5)  # Waktu tunggu antara setiap task dalam detik

    @task
    def test_api(self):
        # URL endpoint
        url = '/v1/ao-fraud/trigger/transaction-member/retail-risk-profile'
        
        # Headers
        headers = {
            'Content-Type': 'application/json',
            'apiKey': 'E97baCBt8SxmDcYNyd3KwbEA0giw8ElF'
        }
        
        # Payload
        payload = {
            "transactionId": "c683852a-0c50-430a-94f2-f62f10ea00c3",
            "corporateName": "PT Jasa Raharja",
            "sourceRequest": "AO-NB",
            "referenceNo": "112024000658"
        }

        # Send POST request
        self.client.post(url, json=payload, headers=headers)
