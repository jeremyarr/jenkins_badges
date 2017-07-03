from setuptools import setup

setup(
    name='jenkins_badges',
    version='1.1.1',
    packages=['jenkins_badges','jenkins_badges.coverage_badge'],
    description="provides badge images based on jenkins data",
    long_description='A flask server that provides badge images based on data from jenkins',
    include_package_data=True,
    install_requires=[
        'flask',
        'requests',
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
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing'
    ]
)

