.. image:: docs/_static/logo_full.png

.. image:: https://badge.fury.io/py/jenkins-badges.svg
    :target: https://badge.fury.io/py/jenkins-badges


`jenkins_badges` is a small flask app that serves dynamic badge images based on data from Jenkins CI.

Supported badges
-----------------
+---------+---------------------------------------------------------------------------------------------------------------+----------------------------------+
|Badge    | Examples                                                                                                      | Default                          |
+=========+===============================================================================================================+==================================+
|coverage | .. image:: https://cdn.rawgit.com/jeremyarr/jenkins_badges/master/docs/_static/coverage_green.svg             | 80% +                            |
+         +---------------------------------------------------------------------------------------------------------------+----------------------------------+
|         | .. image:: https://cdn.rawgit.com/jeremyarr/jenkins_badges/master/docs/_static/coverage_yellow.svg            | 20%-80%                          |
+         +---------------------------------------------------------------------------------------------------------------+----------------------------------+
|         | .. image:: https://cdn.rawgit.com/jeremyarr/jenkins_badges/master/docs/_static/coverage_red.svg               | < 20%                            |
+         +---------------------------------------------------------------------------------------------------------------+----------------------------------+
|         | .. image:: https://cdn.rawgit.com/jeremyarr/jenkins_badges/master/docs/_static/coverage_error.svg             | error getting coverage data      |
+---------+---------------------------------------------------------------------------------------------------------------+----------------------------------+


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


More at https://jenkins-badges.readthedocs.io
----------------------------------------------

Project Links
-------------

- Docs: https://jenkins-badges.readthedocs.io/
- Changelog: https://jenkins-badges.readthedocs.io/en/latest/changelog.html
- PyPI: https://pypi.python.org/pypi/jenkins-badges
- Issues: https://github.com/jeremyarr/jenkins_badges/issues

Kudos
-----

- Idea came from mnpk's `jenkins-coverage-badge <https://github.com/mnpk/jenkins-coverage-badge>`_ written in nodeJS.
- `shields.io <https://shields.io/>`_ for providing scalable badges over a clean API
- `Jenkins <https://jenkins.io/>`_ for being...jenkins

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/jeremyarr/jenkins_badges/blob/master/LICENSE>`_ file for more details.
  




