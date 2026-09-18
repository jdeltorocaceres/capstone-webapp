from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# --------------------------------------------------
# DEMO ONLY - intentionally hardcoded credential
# Cybersecurity Capstone Project
# This key does not provide access to any real service.
# --------------------------------------------------

MONITOR_API_KEY = "DEMO_MONITOR_API_KEY_CAPSTONE_2026"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/status")
def status():
    services = [
        {
            "name": "Portal institucional",
            "status": "Operativo"
        },
        {
            "name": "Servicio de documentos",
            "status": "Operativo"
        },
        {
            "name": "API de monitorización",
            "status": "Operativo"
        },
        {
            "name": "Base de datos",
            "status": "Operativo"
        }
    ]

    return render_template("status.html", services=services)


@app.route("/api/internal/monitor")
def monitor_api():

    supplied_key = request.headers.get("X-API-Key")

    if supplied_key != MONITOR_API_KEY:
        return jsonify({
            "error": "Unauthorized",
            "message": "Valid API key required"
        }), 401

    return jsonify({
        "environment": "production-demo",
        "services": {
            "portal": "operational",
            "documents": "operational",
            "database": "operational"
        }
    })


if __name__ == "__main__":
    app.run(debug=True)
