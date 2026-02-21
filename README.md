# 🌍 World Time API

A minimalist, high-performance microservice built with **FastAPI** to provide real-time date and time information for any valid IANA timezone. Perfect for distributed systems needing a reliable time reference.

---

## 🚀 Quick Start

### Prerequisites

* **Python 3.9+**
* **pip** (Python package manager)

### Installation & Local Deployment

1. **Clone the repository** (or download the files):
```bash
git clone https://github.com/your-username/world-time-api.git
cd world-time-api

```


2. **Install dependencies**:
```bash
pip install -r requirements.txt

```


3. **Run the application**:
```bash
python main.py

```


*The server will start at `http://127.0.0.1:8000*`

---

## 📖 API Documentation

### 1. Get Time by Zone

Retrieves the current local time for a specific geographic region.

* **Endpoint:** `/time/{area}/{city}`
* **Method:** `GET`
* **Parameters:**
* `area` (string): Continent or Ocean (e.g., `Europe`, `America`, `Asia`)
* `city` (string): City name (e.g., `Berlin`, `New_York`, `Tokyo`)



**Example Request:**
`GET /time/Europe/Berlin`

**Success Response (200 OK):**

```json
{
  "timezone": "Europe/Berlin",
  "datetime": "2026-02-21 16:20:00",
  "timestamp": 1771687200.0,
  "iso": "2026-02-21T16:20:00+01:00"
}

```

### 2. Service Status

Checks if the API is online and lists available routes.

* **Endpoint:** `/`
* **Method:** `GET`

---

## 🛠 Advanced Features

### Interactive Documentation

FastAPI automatically generates beautiful, interactive documentation. While the server is running, you can test every endpoint directly in your browser:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Error Handling

The API handles invalid timezone requests gracefully. If an incorrect area or city is provided, you will receive a descriptive error:

**Error Response (404 Not Found):**

```json
{
  "detail": "Timezone 'Mars/Base_Alpha' not found. Please use IANA format (e.g., Europe/London)."
}

```

---

## ☁️ Deployment (Railway.app)

This project is optimized for **Railway**. To deploy:

1. Push this code to a **GitHub** repository.
2. Create a **New Project** on Railway and select "Deploy from GitHub repo".
3. Railway will automatically detect the `requirements.txt` and `Procfile` to start the service.

---
API Docs Are also under /docs
