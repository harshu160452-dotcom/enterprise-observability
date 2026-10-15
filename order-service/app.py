from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "order_service_requests_total",
    "Total requests to order service"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Order Service is running"

@app.route("/health")
def health():
    REQUEST_COUNT.inc()
    return {"status": "healthy", "service": "order-service"}

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
