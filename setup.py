from setuptools import setup

setup(
    name='pyjcb',
    version='1.0',
    packages=['pyjcb'],
    long_description='some description',
    include_package_data=True,
    install_requires=[
        'flask',
        'pyyaml',
        'requests',
    ],
    zip_safe=False,
)

