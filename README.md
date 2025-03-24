Berikut ini adalah contoh **README** dan **description** untuk repositori *Locust Performance Test* yang kamu gunakan di proyek iFG Life, khusus untuk *fraud checking API*. Kamu bisa sesuaikan bagian detail teknis (endpoint, parameter, dsb.) sesuai kebutuhan nanti.

---

### 📝 **Repository Description (untuk GitHub repo)**

> Performance testing scripts using Locust for the Fraud Checking API at iFG Life. This repository is used to simulate and analyze the load handling capabilities of the fraud detection microservices.

---

### 📄 **README.md**

```markdown
# 🚀 iFG Life - Fraud Checking API Performance Test

This repository contains performance test scripts built using [Locust](https://locust.io) to test the scalability and responsiveness of the **Fraud Checking API** at **iFG Life**.

## 📌 Purpose

The goal of this testing suite is to:

- Evaluate the performance and stability of the Fraud Checking API under load.
- Simulate various user loads and traffic patterns.
- Identify potential bottlenecks or failure points before production deployment.

## 🛠️ Tech Stack

- **Locust** – Python-based performance testing tool.
- **Python 3.9+**
- **Docker** (optional, for containerized test runs)

## 📂 Project Structure

```
.
├── locustfile.py         # Main locust test scenarios
├── requirements.txt      # Python dependencies
├── README.md             # Documentation
└── config/               # (Optional) Test configs or payloads
```

## 🚦 How to Run Locust Test

### 1. Clone the Repo

```bash
git clone https://github.com/your-org/fraud-api-performance-test.git
cd fraud-api-performance-test
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Locust

```bash
locust -f locustfile.py
```

Then open your browser at: [http://localhost:8089](http://localhost:8089)

### 4. Run with Docker (optional)

```bash
docker build -t fraud-check-test .
docker run -p 8089:8089 fraud-check-test
```

## 🧪 Example Test Scenarios

- **Single user scenario** – Simulates a single fraud check request.
- **Concurrent fraud checks** – Simulates multiple fraud checks being run in parallel (spike testing).
- **Custom payload test** – Allows custom payload injection for more advanced testing.

## 🔐 Notes

- The actual endpoint and credentials are **not included** in this repository.
- Environment variables or secure vaults (e.g., AWS Secrets Manager) should be used for authentication in real scenarios.

## 📊 Sample Metrics Collected

- Requests per second (RPS)
- Response time distribution
- Error rates
- Throughput under stress

etes?
