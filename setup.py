from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(filepath: str) -> List[str]:
    '''parse requirements from requirements.txt'''

    requirements=[]
    with open(filepath) as f:
        requirements= f.readlines()
        requirements=[r.replace("\n","") for r in requirements]
        
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='MLPROJECTS_deploy',
    version='0.1',
    author='vamshi',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
        
)