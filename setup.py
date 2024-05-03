from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1.0',
    url="https://github.com/Smart-Droplets-Project/smartDropletsDataAdapters",
    author="Mihailo Ilic",
    author_email="mihailo.ilic@vizlore.com",
    packages=find_packages(
        exclude=['test', 'examples']
    ),
    install_requires=[
        'ngsildclient'
    ],
    description="An NGSI-LD Client & Smart Data Models wrapper library, intended for use in the Smart Droplets Project.",
    long_description=open('README.md').read(),
)