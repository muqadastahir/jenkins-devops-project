from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import mysql.connector

app = Flask(__name__)

# Prometheus Metrics
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return "Jenkins CI/CD Pipeline Working Successfully!"

@app.route('/test')
def test():
    return "Flask monitoring working"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
