from setuptools import setup

setup(
    name='jenkins_badges',
    version='1.0',
    packages=['jenkins_badges','jenkins_badges.coverage_badge'],
    long_description='some description',
    include_package_data=True,
    install_requires=[
        'flask',
        'requests',
    ],
    zip_safe=False,
)

