#!/usr/bin/python
import requests
import os, sys
from datetime import datetime, timedelta	
from flask import Flask, request, url_for, redirect, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def rtmp():
    return render_template('rtmp.html')

if __name__ == '__main__':
#	app.run(debug = True)
	app.run(host = '0.0.0.0', port = 3000)
	