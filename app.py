import os
import logging
from datetime import datetime, timezone

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --------------------------------------------------
# AUDIT LOGGING - CAPSTONE DEMONSTRATION
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

audit_logger = logging.getLogger("sigi.audit")


def log_api_access(result, status_code):

    timestamp = datetime.now(timezone.utc).isoformat()

    audit_logger.info(
        "AUDIT timestamp=%s event=monitor_api_access "
        "method=%s path=%s result=%s http_status=%s",
        timestamp,
        request.method,
        
# --------------------------------------------------
# DEMO ONLY - credenciales hardcodeadas intencionalmente como hipótesis
# Cybersecurity Capstone Project
# This key does not provide access to any real service.
# --------------------------------------------------

MONITOR_API_KEY = os.environ.get("MONITOR_API_KEY")


def get_monitoring_data(api_key):
    """
    Simulates an internal monitoring service protected
    by an API key.
    """

    if api_key != MONITOR_API_KEY:
        return None

    return {
        "environment": "production-demo",
        "services": {
            "Portal institucional": "Operativo",
            "Servicio de documentos": "Operativo",
            "API de monitorización": "Operativo",
            "Base de datos": "Operativo"
        }
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/status")
def status():

    # Application authenticates against the monitoring
    # service using the hardcoded API key.
    monitoring_data = get_monitoring_data(MONITOR_API_KEY)

    services = []

    if monitoring_data:
        for name, service_status in monitoring_data["services"].items():
            services.append({
                "name": name,
                "status": service_status
            })

    return render_template("status.html", services=services)


@app.route("/api/internal/monitor")
def monitor_api():

    supplied_key = request.headers.get("X-API-Key")

    monitoring_data = get_monitoring_data(supplied_key)

    if monitoring_data is None:

        log_api_access(
            result="DENIED",
            status_code=401
        )

        return jsonify({
            "error": "Unauthorized",
            "message": "Valid API key required"
        }), 401

    log_api_access(
        result="SUCCESS",
        status_code=200
    )

    return jsonify(monitoring_data)


if __name__ == "__main__":
    app.run(debug=True)
