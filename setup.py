from setuptools import find_packages, setup
from typing import List

E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of required packages
    '''
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if E_DOT in requirements:
            requirements.remove(E_DOT)

    return requirements



setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Nabin',
    author_email = 'nabincoder@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)