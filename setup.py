from setuptools import setup

setup(
    name='pyjcb',
    version='1.0',
    packages=['pyjcb','pyjcb.coverage_badge'],
    long_description='some description',
    include_package_data=True,
    install_requires=[
        'flask',
        'requests',
    ],
    zip_safe=False,
)

