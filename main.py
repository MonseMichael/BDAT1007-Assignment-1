from flask import Flask, render_template, session, request, redirect
from flask import jsonify, url_for
from pymongo import MongoClient
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
from forms import DataForm

app=Flask(__name__)

app.config['SECRET_KEY'] = 'movies'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/read')
def readdata():
    forms = DataForm()
    client = MongoClient("mongodb+srv://Ani:WeatherCan@cluster0.i5fm0.mongodb.net/Movies?ssl=true&ssl_cert_reqs=CERT_NONE")
    db= client["AmazonMovies"]
    col= db["Movies"]
    records = col.find()
    #documents = list(col.find())

    return render_template('readdata.html', records = records)

@app.route('/create', methods=['GET', 'POST'])
def create():
    forms = DataForm()
    if forms.is_submitted():
        result = dict(request.form)
        client = MongoClient("mongodb+srv://Ani:WeatherCan@cluster0.i5fm0.mongodb.net/Movies?ssl=true&ssl_cert_reqs=CERT_NONE")
        db = client["AmazonMovies"]
        col = db["Movies"]
        col.insert(result)
        return render_template('success.html', result = result)

    return render_template('create.html', forms=forms)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    forms = DataForm()
    if forms.is_submitted():
        result = request.form
        client = MongoClient("mongodb+srv://Ani:WeatherCan@cluster0.i5fm0.mongodb.net/Movies?ssl=true&ssl_cert_reqs=CERT_NONE")
        db = client["AmazonMovies"]
        col = db["Movies"]
        col.find_one_and_delete(result)
        return render_template('success.html', result = result)

    return render_template('delete.html', forms=forms)


if __name__ == "__main__":
    app.run(debug=True)
