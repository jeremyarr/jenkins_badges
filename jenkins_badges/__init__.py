'''
`jenkins_badges` is a small flask app that serves dynamic badge images based on data from Jenkins CI.
'''

from .__version__ import __version__

from flask import Flask


def create_app(from_envvar=False, base_url=None, username=None, token=None,
               coverage_yellow=80, coverage_red=20,
               coverage_decimal_points=2):
    '''
    creates the flask application object

    :param from_envvar: if True, configuration parameters are sourced from file referenced by the local JENKINS_BADGES_SETTINGS environmental variable. if False, configuration parameters are sourced from the arguments.
    :type from_envvar: bool

    :param base_url: url of Jenkins instance. Must be supplied if from_envvar=False.
    :type base_url: str

    :param username: username of Jenkins user
    :type username: str

    :param token: token of Jenkins user
    :type token: str

    :param coverage_yellow: threshold for displaying yellow coverage colour. Coverage below this threshold and above the coverage_red threshold will be shown with a yellow background. Coverage above this threshold will be shown with a green background.
    :type coverage_yellow: int

    :param coverage_red: threshold for displaying red coverage colour. Coverage below this threshold will be shown with a red background.
    :type coverage_red: int

    :param coverage_decimal_points: number of decimal points displayed on badge for coverage figure.
    :type coverage_decimal_points: int

    :returns: a flask application object
    '''

    app = Flask(__name__)

    app.config['JENKINS_BASE_URL'] = base_url
    app.config['JENKINS_USERNAME'] = username
    app.config['JENKINS_TOKEN'] = token
    app.config['COVERAGE_YELLOW'] = coverage_yellow
    app.config['COVERAGE_RED'] = coverage_red
    app.config['COVERAGE_DECIMAL_POINTS'] = coverage_decimal_points

    if from_envvar:
        app.config.from_envvar('JENKINS_BADGES_SETTINGS')

    if 'JENKINS_BASE_URL' not in app.config or app.config['JENKINS_BASE_URL'] is None:
        raise ValueError("must supply a valid base url for the jenkins instance")

    from jenkins_badges.coverage_badge import coverage_badge
    app.register_blueprint(coverage_badge)

    return app
