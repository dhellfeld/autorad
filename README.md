# autorad

## Description
Framework for autonomous radiological source search algorithms.

## Installation
Once all dependencies have been successfully installed (see below), simply run the following:
```
$ python setup.py install
```
If you wish to make changes to this repo and want those changes updated in your install, change `install` to `develop` in the command above.

## Dependencies
The current list of dependencies is as follows:
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)

### Anaconda
A `conda` environment files exist (`env.yml`) for your convenience to install the dependencies of `autorad` into a self-contained environment without having any effect on any previously installed packages. Assuming `anaconda` has already been [installed on your machine](https://docs.anaconda.com/anaconda/install/), simply run the command
```
$ conda env create -f env.yml
```
The environment will be named `autorad`. To activate the environment, run the following
```
$ conda activate autorad
```
Make sure this environment is activated when `setup.py` is run.

### Manually
If you prefer to install the dependencies outside of an environment:
```
$ pip install -r requirements.txt
```

## Structure
Write me...

## Examples
Write me...
