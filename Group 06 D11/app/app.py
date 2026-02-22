from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v1")

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Manufacturing Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                text-align: center;
                padding-top: 50px;
            }
            .card {
                background: white;
                padding: 30px;
                margin: auto;
                width: 450px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
            }
            .version {
                font-size: 18px;
                margin: 15px 0;
            }
            button {
                padding: 10px 20px;
                background: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 14px;
            }
            button:hover {
                background: #2980b9;
            }
            footer {
                margin-top: 20px;
                font-size: 12px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Manufacturing System Dashboard</h1>
            <p class="version"><strong>Application Version:</strong> {{version}}</p>
            <p>System Status: Running</p>
            <a href="/status"><button>Check Machine Status</button></a>
            <footer>
                Kubernetes Deployed | Zero-Downtime Enabled
            </footer>
        </div>
    </body>
    </html>
    """, version=VERSION)


@app.route("/status")
def status():
    return jsonify({
        "machine": "operational",
        "temperature": "normal",
        "version": VERSION
    })


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
