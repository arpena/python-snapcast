from setuptools import setup

setup(
    name='snapcast',
    version='2.3.6',
    description='Control Snapcast.',
    url='https://github.com/arpena/python-snapcast/',
    license='MIT',
    author='happyleaves',
    author_email='arpena@gmail.com',
    packages=['snapcast', 'snapcast.control', 'snapcast.client'],
    install_requires=[
        'construct>=2.5.2',
        'packaging',
        'websockets',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)
