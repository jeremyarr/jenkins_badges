from flask import send_file, Blueprint,current_app
import requests
import io
from collections import namedtuple

Coverage = namedtuple("Coverage",["formatted","colour"])

coverage_badge = Blueprint('coverage_badge',__name__)

@coverage_badge.route("/coverage/<job_name>",methods=['GET'])
def send_coverage_badge(job_name):
    if job_name == "favicon.ico":
        return "",200

    jurl = generate_jenkins_api_url(job_name)
    auth = (current_app.config['JENKINS_USERNAME'],
            current_app.config['JENKINS_TOKEN'])
    auth = None if auth==(None,None) else auth
    jresp = requests.get(jurl,auth=auth)
    print("GET {} {}".format(jresp.status_code, jurl))
    if jresp.status_code != 200:
        return send_error_badge()

    cov = extract_coverage(jresp)
    surl = generate_shields_url(cov)
    sresp = requests.get(surl, stream=True)
    print("GET {} {}".format(sresp.status_code,surl))
    if sresp.status_code != 200:
        return send_error_badge()

    path = io.BytesIO(sresp.content)
    print("SENDING coverage badge of {}".format(cov.formatted))
    return send_file(path, mimetype="image/svg+xml",cache_timeout=30), 200

def send_error_badge():
    path = "coverage_badge/static/error_badge.svg"
    print("SENDING access fail badge")
    return send_file(path, mimetype="image/svg+xml",cache_timeout=30), 200

def generate_jenkins_api_url(job_name):
    return ("{}/job/{}/"
           "lastSuccessfulBuild/cobertura/api/json/?depth=2"
           "").format(current_app.config["JENKINS_BASE_URL"],job_name)

def extract_coverage(jresp):
    coverage_dict = jresp.json()
    for d  in coverage_dict['results']['elements']:
        if d['name'] == "Lines":
            cov_raw = d['ratio']
            colour = get_colour(cov_raw)
            formatted = "{:.2f}%".format(cov_raw)
            return Coverage(formatted=formatted,colour=colour)

def generate_shields_url(c):
    return ("https://img.shields.io/badge/coverage-{}25-{}.svg"
            "?maxAge=2".format(c.formatted,c.colour))

def get_colour(cov_raw):
    if cov_raw < 20:
        return "red"
    elif cov_raw < 80:
        return "yellow"
    else:
        return "brightgreen"