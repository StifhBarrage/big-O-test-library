import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.3'
PACKAGE_NAME = 'big_O_test' 
AUTHOR = 'Herless Stifh Barragán León'
AUTHOR_EMAIL = 'hbarraganl@unal.edu.co'
URL = 'https://github.com/StifhBarrage/big-O-test-library' 

LICENSE = 'MIT' 
DESCRIPTION = 'Librería para para comparar rendimiento entre dos algoritmos' 
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"


INSTALL_REQUIRES = [
      'big_O'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
