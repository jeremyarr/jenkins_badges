'''
hello 123
'''
from flask import Flask

def create_app(base_url=None,username=None,token=None):
    '''
    creates the flask application object
    username: jenkins username
    token: username token
    base url: jenkins base url
    '''
    app = Flask(__name__)
    if not base_url:
        app.config['JENKINS_USERNAME'] = None
        app.config['JENKINS_TOKEN'] = None
        app.config.from_envvar('JENKINS_BADGES_SETTINGS')
        assert "JENKINS_BASE_URL" in app.config
    else:
        app.config['JENKINS_BASE_URL'] = base_url
        app.config['JENKINS_USERNAME'] = username
        app.config['JENKINS_TOKEN'] = token

    from jenkins_badges.coverage_badge import coverage_badge
    app.register_blueprint(coverage_badge)

    return app

