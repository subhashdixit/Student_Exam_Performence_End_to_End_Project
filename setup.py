from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .' # When installed -e . will get mapped to setup.py and all the information gets stored
def get_requirements(file_path:str)->List[str]:
    """This function will give the list of requirements """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # \n will get recorded as well
        requirements = [req.replace("\n","") for req in requirements] # Replacing \n with blank space to read the requirments.txt fle
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) # Remove -e . because it will get triggered in set.py and will cause error
    return requirements
setup(
name = 'Student_Exam_Performence_End_to_End_Project',
version = '0.0.1',
author = "Subhash",
author_email = "subhashdixit17@gmail.com",
packages = find_packages(), # It will consdier src as the packages. Wherever __innit__ will be there
# install_requires = ['pandas','numpy','seaborn'] # cannot write all the packages manuaaly, so we create a function
install_requires = get_requirements("requirements.txt")
)

