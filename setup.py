from setuptools import setup,find_packages
import codecs
import os
here= os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"),encoding="utf-8") as fh:
    long_description='\n'+fh.read()
DESCRIPTION='python for excel'
setup(
    name='NHV_Style',
    version='0.1.0',
    author_email='<mobahoangvu2004@gmail.com>',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,
    package=find_packages(),
    install_requires=['pandas','xlwings'],
    keywords=['python','python NHV_Style'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programing Langue :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)