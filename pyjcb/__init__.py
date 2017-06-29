from flask import Flask,redirect,send_file
import requests
import json
import yaml
import os
import traceback
import shutil
import io
from collections import namedtuple
app = Flask(__name__)

Coverage = namedtuple("Coverage",["formatted","colour"])
error_badge = "https://img.shields.io/badge/coverage-accessfail-lightgrey.svg?maxAge=30"

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

@app.route("/<job_name>",methods=['GET'])
def send_badge(job_name):
    try:
        conf_data = get_conf_data()
        print("job name1={}".format(job_name))
        jenkins_api_url = generate_api_url(job_name,conf_data)
        print(jenkins_api_url)
        if conf_data['username'] and conf_data['token']:
            jenkins_resp = requests.get(jenkins_api_url,auth=(conf_data['username'],conf_data['token']))
        else:
            jenkins_resp = requests.get(jenkins_api_url)

        print("jenkins resp = {}".format(jenkins_resp.text))
        coverage_dict = jenkins_resp.json()
        c = extract_coverage(coverage_dict)
        badge_url = generate_badge_url(c)
        print("generated badge {}".format(badge_url))
        badge_resp = requests.get(badge_url,stream=True)
        print(badge_resp.content)

        full_file_path = io.BytesIO(badge_resp.content)
        resp = send_file(full_file_path, mimetype="image/svg+xml",cache_timeout=30)
        print(resp.headers)
        return resp
    except Exception as e:
        tb_str = traceback.format_exc()
        print(tb_str)
        full_file_path = "{}/error_badge.svg".format(APP_ROOT)
        return send_file(full_file_path, mimetype="image/svg+xml",cache_timeout=30)

def get_conf_data():
    full_file_path = "{}/pyjcb.yaml".format(APP_ROOT)
    prod_full_file_path = "{}/prod_pyjcb.yaml".format(APP_ROOT)
    if os.path.isfile(prod_full_file_path):
        full_file_path = prod_full_file_path

    with open(full_file_path,"r") as f:
        conf_data = yaml.load(f)

    return conf_data

def generate_api_url(job_name,conf_data):
    base_url = conf_data["jenkins_base_url"] 

    print("job name2={}".format(job_name))

    return ("{}/{}/"
           "lastSuccessfulBuild/cobertura/api/json/?depth=2"
           "").format(base_url,job_name)

def extract_coverage(coverage_dict):
    for d  in coverage_dict['results']['elements']:
        if d['name'] == "Lines":
            cov_raw = d['ratio']
            colour = get_colour(cov_raw)
            formatted = "{:.2f}%".format(cov_raw)
            return Coverage(formatted=formatted,colour=colour)

def generate_badge_url(c):
    return ("https://img.shields.io/badge/coverage-{}25-{}.svg"
            "?maxAge=2".format(c.formatted,c.colour))

def get_colour(cov_raw):
    if cov_raw < 20:
        return "red"
    elif cov_raw < 80:
        return "yellow"
    else:
        return "brightgreen"

if __name__ == "__main__":
    app.run()