# Introduction
This is a primary introduction to molecule, an Ansible molecule which provides unit-testing capabilities to Ansible roles.

## Installation
This installation guide assumes that `virtualenv` and `docker` are  installed. Python >3.5 is expected.
The rough outline is as followed:
- Creating a Python `virtualenv`;
- Activating and leaving a virtualenv;
- Install Ansible in the virtualenv;
- Install molecule in the virtualenv;

### Creating a Python `VirtualEnv`
A Python `virtualenv` should be seen as an additional installation of Python in a clean environment. We will modify this version by installing Ansible and Molecule, but by
using a VirtualEnv we will make sure that we contain the changes and do not change the behaviour of the default Python installation.

This can also be compared by installing a new application in a seperate virtual-machine. This allows you to try out the application, but at thesame time you make sure the application doesn't break existing stuff as it's virtualized in a seperate host.

Creating a VirtualEnv is quite easy:
```bash
# Command skeleton structure
virtualenv <name of virtualenv> -p < path to python install > 

# Example
virtualenv my-molecule-env -p $(which python3)
```

### Activating and leaving a virtualenv
After you have crated a virtualenv, you will notice that there's a new directory in your current working directory:
```bash
➜  ls
my-molecule-venv
```
Great. In order to use our new virtualenvironment, we have to activate (or 'source') it. However, before I do this, i'll show you something noteable before I enter the VirtualEnv:
```bash
➜  cd my-molecule-venv
➜  my-molecule-venv # before I activate the virtual-env
➜  my-molecule-venv python -V
Python 2.7.16
```
Before entering the virtual environment, `python -v` resolves to python version 2.7.16. Now let's try thesame thing in my virtual environment. 
Again, a virtual environment can be put into work by sourcing or activating it. Notice the prompt once it does get activated.

```bash
# Source / Activate the VirtualEnv 
➜  my-molecule-venv # activate/source the virtual env     
➜  my-molecule-venv source bin/activate 
(my-molecule-venv) ➜  my-molecule-venv 
(my-molecule-venv) ➜  my-molecule-venv # Now let's examine the current Python version
(my-molecule-venv) ➜  my-molecule-venv python -V
Python 3.7.3
```
Notice the change in Python version inside and outside the virtual-environment. Finally, you'll probably want to know how to exit the virtual environment.

```bash
(my-molecule-venv) ➜  my-molecule-venv deactivate
➜  my-molecule-venv 
```
Notice how the prompt changes again to signal you've left the virtual environment by entering thew `deactivate` command. 

