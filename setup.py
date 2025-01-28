from setuptools import setup, find_packages

setup(
    name='sd_data_adapter',
    url="https://github.com/Smart-Droplets-Project/smartDropletsDataAdapters",
    author="Mihailo Ilic",
    author_email="mihailo.ilic@vizlore.com",
    packages=find_packages(
        include=['sd_data_adapter*']
    ),
    install_requires=[
        'ngsildclient'
    ],
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    description="An NGSI-LD Client & Smart Data Models wrapper library, intended for use in the Smart Droplets Project.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
)