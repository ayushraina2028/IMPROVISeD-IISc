# Project Name

This repository contains a tool that uses Python and C++ libraries to solve various problems involving Semidefinite Programming (SDP). It integrates MOSEK, a powerful C++ library for SDP, along with other Python tools like PyMOL for visualization.

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
