from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'jenkins_badges', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name='jenkins_badges',
    version=about['__version__'],
    packages=['jenkins_badges','jenkins_badges.coverage_badge'],
    description="provides badge images based on jenkins data",
    long_description='A flask server that provides badge images based on data from jenkins',
    include_package_data=True,
    install_requires=[
        'flask',
        'requests',
        'six',
    ],
    zip_safe=False,
    author="Jeremy Arr",
    author_email="jeremyarr@gmail.com",
    license="MIT",
    keywords=["jenkins", 
              "coverage",
              "cobertura",
              "badges",
              "shields",
              "github"],
    url="https://github.com/jeremyarr/jenkins_badges",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing'
    ]
)

