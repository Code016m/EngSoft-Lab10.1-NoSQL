from flask import Flask
from catalogo.routes import catalogo_bp

app = Flask(__name__)

app.secret_key = "chave-local-desenvolvimento"

app.register_blueprint(catalogo_bp)

if __name__ == "__main__":
    app.run(debug=True)
