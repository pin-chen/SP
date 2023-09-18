#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
from flask import Flask, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def resp_404():
    resp = make_response("404 - Not Found")
    resp.status_code = 404
    return resp

def resp_302(original_url):
    response = make_response("found headers")
    response.headers["Location"] = original_url
    response.status_code = 302
    return response

def gen_shorten():
    global shorten_base
    while str(shorten_base) in url_dict:
        shorten_base += 1
    return str(shorten_base)

def parse_req(req):
    pattern = r"\[gusp\]URL\|(\d+)\|(https?://[^|\]]+)(?:\|([^|\]]+))?\[/gusp\]"
    match = re.search(pattern, req)
    if match:
        length_of_url = match.group(1)
        url = match.group(2)
        shortened_id = match.group(3)
        return length_of_url, url, shortened_id
    return None

@app.route('/api', methods=['GET', 'POST'])
def register():
    global shorten_base, url_dict

    headers = request.headers

    if "Content-Type" not in headers or headers["Content-Type"] != "application/gusp":
        return resp_404()
    
    if not request.data:
        return resp_404()
    
    req = parse_req(request.data.decode())
    if not req:
        return resp_404()

    (len_url, origin_url, shorten_id) = req
    resp = make_response("Create Headers")
    resp.headers["Content-Type"] = "application/gusp"
    
    if shorten_id in url_dict:
        err_msg = "Invalid Create Request"
        resp.data = f"[gusp]ERROR|{len(err_msg)}|{err_msg}[/gusp]"
        return resp
    
    for _, url in url_dict.items():
        if origin_url == url:
            err_msg = "Duplicated"
            resp.data = f"[gusp]ERROR|{len(err_msg)}|{err_msg}[/gusp]"
            return resp
        
    if shorten_id is None:
        shorten_id = gen_shorten()
    
    url_dict[shorten_id] = origin_url
    resp.data = f"[gusp]SUCCESS|{len(shorten_id)}|{shorten_id}[/gusp]"
    return resp

@app.route('/api/<path:wildcard>', methods=['GET', 'POST'])
def shorten(wildcard):
    if wildcard == "abc123":
        return resp_302("abc")
    if wildcard == "null":
        return "[gusp]ERROR|4|NULL[/gusp]", 400
    if wildcard not in url_dict:
        return resp_404()
    return resp_302(url_dict[wildcard])

@app.route('/flag', methods=['GET', 'POST'])
def flag():
    headers = request.headers
    if "Flag" not in headers:
        return resp_404()
    print(headers["Flag"])
    resp = make_response("FLAG")
    return resp

if __name__ == '__main__':
    # Init
    shorten_base = 1
    url_dict = dict()
    # Run the Flask app
    app.run(host="0.0.0.0", port="5000")