# pyjcb
A teeny tiny flask server that returns a badge image based on jenkins cobertura coverage data for a job

Requirements
-------------
- Jenkins
- Jenkins cobertura plugin
- requests
- pyyaml
- flask

Quickstart
-----------
**In editor:**

1. edit pyjcb.yaml file with the url of your jenkins instance

**In Terminal:**

2. navigate to pyjcb directory

3. export FLASK_APP=main.py

4. export FLASK_DEBUG=1

5. flask run

**In Browser:**

6: http://localhost:5000/<JenkinsJobName>





