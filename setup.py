from setuptools import setup, find_packages

setup(
    name='CloudPhoto',
    version='0.1.0',
    author='Taliya Arsembekova',
    packages=find_packages(),
    install_requires=['click', 'boto3'],
    entry_points={
        'console_scripts': [
            'cloudphoto = cloudphoto.main:main',
        ]
    }
)
