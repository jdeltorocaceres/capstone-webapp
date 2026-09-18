from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
