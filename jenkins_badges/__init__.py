__version__ = "1.1.0"
'''
hello 123
'''
from flask import Flask


def create_app(from_envvar=False,base_url=None,username=None,token=None,
               coverage_yellow=None, coverage_red=None,
               coverage_decimal_points=None):
    '''
    creates the flask application object
    username: jenkins username
    token: username token
    base url: jenkins base url
    '''
    app = Flask(__name__)
    app.config.from_object('jenkins_badges.default_settings')

    if from_envvar:
        app.config.from_envvar('JENKINS_BADGES_SETTINGS')
        assert "JENKINS_BASE_URL" in app.config
    else:
        if base_url is None:
            raise ValueError("must supply base_url if from_envvar is False")

        app.config['JENKINS_BASE_URL'] = base_url

        if username is not None:
            app.config['JENKINS_USERNAME'] = username
        if token is not None:
            app.config['JENKINS_TOKEN'] = token
        if coverage_yellow is not None:
            app.config['COVERAGE_YELLOW'] = coverage_yellow
        if coverage_red is not None:
            app.config['COVERAGE_RED'] = coverage_red
        if coverage_decimal_points is not None:
            app.config['COVERAGE_DECIMAL_POINTS'] = coverage_decimal_points


    from jenkins_badges.coverage_badge import coverage_badge
    app.register_blueprint(coverage_badge)

    return app


