from setuptools import setup, find_packages

setup(
    name='whoareu',
    version='0.1.0',
    description='See information about yourself',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'python-dotenv'
    ]
)
