import os
from flask import Flask, render_template, request
from calculator import sumar, restar, multiplicar, dividir

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operacion"]
            if op == "sumar":
                resultado = sumar(num1, num2)
            elif op == "restar":
                resultado = restar(num1, num2)
            elif op == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif op == "dividir":
                resultado = dividir(num1, num2)
        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Ingresa números válidos"
    return render_template("index.html", resultado=resultado, error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
