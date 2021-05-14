# Project 2 Portfilio  

## Team

Kyle Chang  
Christian Warren  
Dev Vadalia  

## Data

### Group A

VFIAX, VBTLX, VGSLX

### Group B

VIMAX, VSMAX, VGHCX  

### Group C

AMZM, WMT, CVS

## Init instructions

Requires Python, pip, before you get started. All dependancies are in requirements.txt. Install Instructions:

```sh
make init
```

will install all requirements in requirements.txt  

```sh
make clean
```

will clean any python residuals, like precompiled python files.  

To run the .ipynb files you need Jupyter Labs installed. it is located in requirements.txt as well. if you have VS code you can read them, or you can run 

```sh
jupyter lab
```

in a terminal and use jupyter in a browser window.

## for Homework 6

you need to enable matlab input with python.

to find your matlabroot, launch matlab and execute

```matlab
matlabroot
```

and it will output the directory path. this is required for homeworks 6, 7, and 8, as well as the project to calcuate the QUADPROG.

```sh
cd matlabroot/extern/engines/python
python setup.py install
```

## Homework PDFs

The PDFs we submitted are located located in ``/Homework Submissions``

## If you have any questions feel free to email us
