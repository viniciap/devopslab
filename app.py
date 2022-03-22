from flask import Flask

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/")
def pagina_inicial():
    return "Hello World - Vinícius Ciappina Pereira"

if __name__ == '__main__':
    app.run()