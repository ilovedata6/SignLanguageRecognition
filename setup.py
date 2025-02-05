from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line and not line.startswith('#')]

setup(
    name='signLanguageRecognition',
    version='0.1.0',
    author='Bilal Saeed',
    author_email='ibilalsaeed@outlook.com',
    description='A sign language recognition system using deep learning and computer vision.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ilovedata6/signLanguageRecognition',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
