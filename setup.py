from setuptools import find_packages, setup

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Nabin',
    author_email = 'nabincoder@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas', 'numpy', 'seaborn']
)