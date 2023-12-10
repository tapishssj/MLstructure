from setuptools import find_packages, setup
from  typing import List

HYPHEN_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]: 

    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[rq.replace('/n',"") for rq in requirements]

        if HYPHEN_e_dot in requirements:
            requirements.remove(HYPHEN_e_dot)

    return requirements


setup(
    name = 'MLproject',
    version='0.0.1',
    author='Tapish',
    author_email='Tapish360z@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
