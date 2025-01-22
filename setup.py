## Build machine learning project as a package so that other users can use it directly
from setuptools import find_packages,setup
from typing import List

to_remove = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if to_remove in requirements:
            requirements.remove(to_remove)
    return requirements

setup(
    name = 'ML_project',
    version='0.0.1',
    author='Nishchay Singla',
    author_email='nishchaysingla1234@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)