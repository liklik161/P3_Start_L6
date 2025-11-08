from django.shortcuts import render
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/over")
def over():
    return render_template("over.html")
@app.route("/gebruiker/<naam>")
def gebruiker_profiel(naam):
    return render_template("profiel.html", gebruiker_profiel=naam)
if __name__ == "__main__":
   app.run(debug=True)