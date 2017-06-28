from flask import Flask,redirect
import requests
import json
import yaml
import os
import traceback
from collections import namedtuple
app = Flask(__name__)

Coverage = namedtuple("Coverage",["formatted","colour"])
error_badge = "https://img.shields.io/badge/coverage-accessfail-lightgrey.svg?maxAge=30"

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

@app.route("/<job_name>",methods=['GET'])
def send_badge(job_name):
    try:
        jenkins_api_url = generate_api_url(job_name)
        jenkins_resp = requests.get(jenkins_api_url)
        print("jenkins resp = {}".format(jenkins_resp.text))
        coverage_dict = jenkins_resp.json()
        c = extract_coverage(coverage_dict)
        badge_url = generate_badge_url(c)
        print("generated badge {}".format(badge_url))
        return redirect(badge_url)
    except Exception as e:
        tb_str = traceback.format_exc()
        print(tb_str)
        return redirect(error_badge)

def generate_api_url(job_name):
    full_file_path = "{}/pyjcb.yaml".format(APP_ROOT)
    prod_full_file_path = "{}/prod_pyjcb.yaml".format(APP_ROOT)
    if os.path.isfile(prod_full_file_path):
        full_file_path = prod_full_file_path

    with open(full_file_path,"r") as f:
        conf_data = yaml.load(f)
        base_url = conf_data["jenkins_base_url"] 

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
            "?maxAge=30".format(c.formatted,c.colour))

def get_colour(cov_raw):
    if cov_raw < 20:
        return "red"
    elif cov_raw < 80:
        return "yellow"
    else:
        return "brightgreen"

if __name__ == "__main__":
    app.run()