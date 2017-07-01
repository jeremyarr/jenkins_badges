
.. image:: _static/logo_full.png

welcome to jenkins_badges
==========================

Current version: v\ |version|.

`jenkins_badges` is a small flask app that provides dynamic badge images based on data from Jenkins CI.

.. contents::
   :local:
   :depth: 1

Supported badges
-----------------

+---------+----------------------------------------+----------------------------------+
|coverage | .. image:: _static/coverage_green.svg  | default: 80% +                   |
+         +----------------------------------------+----------------------------------+
|         | .. image:: _static/coverage_yellow.svg | default: 20%-80%                 |
+         +----------------------------------------+----------------------------------+
|         | .. image:: _static/coverage_red.svg    | default: < 20%                   |
+         +----------------------------------------+----------------------------------+
|         | .. image:: _static/coverage_error.svg  | error getting coverage data      |
+---------+----------------------------------------+----------------------------------+


Get it now
-----------

With pip:
**********

.. code-block:: bash

    $ pip install jenkins_badges

Jenkins Requirements
----------------------
`jenkins_badges` communicates with your Jenkins instance over the `Jenkins API <https://wiki.jenkins.io/display/JENKINS/Remote+access+API>`_ . You need to either set up up the `anonymous` user in Jenkins with read access or supply `jenkins_badges` with the credentials of a jenkins user who has read access.

For the coverage badge to work, your Jenkins instance must have the `Cobertura plugin <https://wiki.jenkins.io/display/JENKINS/Cobertura+Plugin>`_ installed with coverage data being supplied to it after every successful build.

You can test out whether `jenkins_badges` will be able to communicate with Jenkins by performing the following API request:

Linux:

.. code-block:: bash

    $ curl http<s>://<path to your jenkins instance>/job/<job name>/lastSuccessfulBuild/cobertura/api/json/?depth=2

Sample Output:

.. code-block:: console

    {"_class":"hudson.plugins.cobertura.targets.CoverageResult","results":{"children":[{"children":[{}],"elements":[{},{},{},{}],"name":"marbl"}],"elements":[{"denominator":1.0,"name":"Packages","numerator":1.0,"ratio":100.0},{"denominator":1.0,"name":"Files","numerator":1.0,"ratio":100.0},{"denominator":1.0,"name":"Classes","numerator":1.0,"ratio":100.0},{"denominator":5.0,"name":"Lines","numerator":4.0,"ratio":80.0},{"denominator":0.0,"name":"Conditionals","numerator":0.0,"ratio":100.0}],"name":"Cobertura Coverage Report"}}

Quickstart
----------

`jenkins_badges` needs to be provided with information about your jenkins instance. This can be provided as arguments to the `create_app` function or via a configuration file.

Supplying configuration parameters directly
**********************************************

1. create and run the app

.. code-block:: python

    import jenkins_badges

    #path to your jenkins instance
    base_url = "https://example.com/jenkins" 

    # not required if anonymous jenkins user has read access
    username = "apiuser" #a user with read access
    token = "6c3bde145bcda49402b6914f2353a734" #user's token

    app = jenkins_badges.create_app(base_url=base_url,
                                    username=username,
                                    token=token)
    app.run()

Output:

.. code-block:: console

    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2. Your coverage badge image should be accessible at `http://127.0.0.1:5000/coverage/<JenkinsJobName>`



Supplying a configuration file
************************************

1. Create a configuration file

.. code:: python

    # /home/ubuntu/.jenkins_badges
    JENKINS_BASE_URL = "https://example.com/jenkins"

    # not required if anonymous jenkins user has read access
    JENKINS_USERNAME = "apiuser" #a user with read access
    JENKINS_TOKEN = "6c3bde145bcda49402b6914f2353a734" #user's token

2. Create a JENKINS_BADGES_SETTINGS environmental variable with the path to the configuration file:

Linux:

.. code-block:: bash

    $ export JENKINS_BADGES_SETTINGS=/home/ubuntu/.jenkins_badges

3. create and run the app

.. code-block:: python

    import jenkins_badges

    app = jenkins_badges.create_app()
    app.run()

Output:

.. code-block:: console

    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


4. Your coverage badge image should be accessible at `http://127.0.0.1:5000/coverage/<JenkinsJobName>`


Placing into a Readme File
---------------------------
Displaying a badge is as easy as placing a reference into your readme file.

If your readme file uses MarkDown:

.. code-block:: md

    ![Coverage](http://127.0.0.1:5000/coverage/<JenkinsJobName>)

If your readme file uses restructuredText:

.. code-block:: rst

    .. image:: http://127.0.0.1:5000/coverage/<JenkinsJobName>

WSGI Example
-------------

Just like any Flask app, a `jenkins_badges` app can be placed on a server with WSGI support,
by creating a wsgi file:

.. code:: python

    #exampleapp.wsgi

    import os

    #tell jenkins_badges where the config file is located
    os.environ['JENKINS_BADGES_SETTINGS'] = '/home/ubuntu/.jenkins_badges'

    from jenkins_badges import create_app

    #name of app must be "application"
    application = create_app()


Responsiveness
---------------
`jenkins_badges` serves badge images with a "maxAge" `cache-control` header value of 30 seconds. As long as the server hosting your documentation respects `cache-control` headers, your badge should update on a page refresh after a jenkins build.

The responsiveness of images served by `jenkins_badges` has been successfully tested on readme pages hosted by GitHub.


Project info
------------

.. toctree::
   :maxdepth: 1

   changelog
   license
   authors
   kudos
