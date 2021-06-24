import dataiku
#import pandas as pd
from flask import request
import requests
import re
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse


@app.route('/test')
def test():
    print ("TEST")
    return "TEST"

@app.route('/<path:url>')
#@app.route('/cluster/<path:url>')
def reverse_proxy(url):
    #print ("before ",url)
       
    return url
