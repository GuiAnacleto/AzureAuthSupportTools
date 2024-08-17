from setuptools import setup, find_packages

setup(
    name='gandalf-customerservice',
    version='0.1',
    py_modules=['cli'],
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    install_requires=[
        'click',
        'msal',
        'python-dotenv'
    ],
    entry_points='''
        [console_scripts]
        galf=infrastructure.entrypoints.cli.cli:cli
    ''',
)
