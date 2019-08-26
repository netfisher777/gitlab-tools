from setuptools import setup, find_packages

setup(
    name='glt',
    version='0.1',
    packages=find_packages(),
    py_modules=['cli'],
    install_requires=[
        'click',
        'python-gitlab'
    ],
    entry_points='''
        [console_scripts]
        glt=cli:glt
    ''',
)
