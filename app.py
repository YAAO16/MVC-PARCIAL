from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template("views/inicio.html")

if __name__ == '__main__':
    app.secret_key = "kamata16angulo"
    app.run(debug=True)