import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Mi App en GCP</title>
    <style>
        body { font-family: Arial; background: #1a1a2e; color: #eee;
               display: flex; justify-content: center; align-items: center;
               height: 100vh; margin: 0; }
        .card { background: #16213e; padding: 40px; border-radius: 16px;
                text-align: center; box-shadow: 0 8px 32px rgba(0,0,0,.3); }
        h1 { color: #00d4ff; }
        p { color: #aaa; }
    </style></head>
    <body><div class="card">
        <h1>🚀 ¡Hola desde Cloud Run!</h1>
        <p>Deploy automático por Aldo Ortiz</p>
        <p>Versión: 1.0</p>
    </div></body></html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
