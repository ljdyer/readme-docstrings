from setuptools import setup

setup(
    name='readme_docstrings',
    version='1.4',
    description='Pull docstrings from Python code files into markdown files',
    author='Laurence Dyer',
    author_email='ljdyer@gmail.com',
    url='https://github.com/ljdyer/readme-docstrings',
    packages=['readme_docstrings'],
    entry_points={
        'console_scripts': [
            'readme_docstrings = readme_docstrings.main:readme_docstrings'
        ]
    }
)
