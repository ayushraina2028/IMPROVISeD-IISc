# Integrated Modelling of Protein Complexes Via Single Shot Registration Using Dream (IMPROVISeD)

This repository contains a tool that uses Python and C++ libraries to model the structure of Protein Complexes using a class of optimization technique known as semidefinite programming (SDP). It integrates MOSEK, a powerful C++ library for SDP, along with other Python tools like PyMOL for visualization.

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
  - [Python Packages](#python-packages)
  - [MOSEK Installation](#mosek-installation)
- [MOSEK Setup](#mosek-setup)
  - [License Setup](#license-setup)
- [Usage](#usage)
- [Example Usage](#example-usage)
- [Instructions](#instructions)
  - [Installing Dependencies](#installing-dependencies)
  - [Running the Tool](#running-the-tool)
  - [Visualizing with PyMOL](#visualizing-with-pymol)
- [License](#license)

## Installation

To install the necessary dependencies for running this tool, please follow the instructions below:


### Requirements

#### Python Packages

The tool requires the following Python packages to be installed:

- `numpy`
- `biopython`
- `pandas`
- `scipy`
- `pymol` (PyMOL must be installed separately; see details below)

To install the Python dependencies (excluding PyMOL), run:

```sh
pip install -r requirements.txt
```

#### MOSEK Installation
This tool requires MOSEK C++ library to run. You need to download it and install it using the instructions provided https://docs.mosek.com/latest/cxxfusion/install-interface.html
You also need to obtain a license for mosek, checkout section 4.3 from https://docs.mosek.com/10.2/install/installation.html
You will find a folder named "mosek" when you do the above 2 steps properly, place this folder in the Packages directory of the project.

#### Mosek License File
Trial License is the easiest to obtain, whose validity is 30 days. 

#### Compiling using Mosek
You can find the compilation command using mosek in this link https://docs.mosek.com/latest/cxxfusion/install-interface.html 
It will be something like 
```sh
g++ -std=c++11 register.cpp -o register -I../../Packages/mosek/10.2/tools/platform/linux64x86/h -L../../Packages/mosek/10.2/tools/platform/linux64x86/bin -Wl,-rpath-link,../../Packages/mosek/10.2/tools/platform/linux64x86/bin -Wl,-rpath=../../Packages/mosek/10.2/tools/platform/linux64x86/bin -lmosek64 -lfusion64
```
when mosek is placed in Packages Directory. You need to compile the Registration/CodeFile/register.cpp file using above command. One executable is already present but if at the time of running the tool, the version of mosek is changed then you need to do compilation and obtain your own license to run the tool. 
For easy usage, I have included both mosek package and a license "mosek.lic" with this tool. If at the time of running the tool, some update of mosek is released then it will give error. In that case please remove mosek library from the Packages folder and do the installation steps as shown above, with a freshly obtained license. (In the case you need to put newly obtained mosek folder in the Packages directory)

#### Eigen Package
This package is also required to run the tool, this is already included in Packages folder for use.