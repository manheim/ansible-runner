# ansible-runner.py

Python helper script to install ansible in a virtual environment, install roles, and run a playbook


## Usage

```
usage: ansible-runner.py [-h] [-i INSTALL_DIR] [-c] [-v VENV_VERSION]
                         [-a ANSIBLE_REQUIREMENT] [-r REQUIREMENTS]
                         [-p PLAYBOOK] [-e]

Python helper script to install ansible in a virtual environment, install
roles, and run a playbook

optional arguments:
  -h, --help            show this help message and exit
  -i INSTALL_DIR, --install-dir INSTALL_DIR
                        Install dir for ansible virtual environment. Defaults
                        to ".ansible-runner"
  -c, --clean           Clean the install dir, if it exists, and reinstall
                        roles
  -v VENV_VERSION, --venv-version VENV_VERSION
                        Virtualenv version to use. Defaults to "16.1.0"
  -a ANSIBLE_REQUIREMENT, --ansible-requirement ANSIBLE_REQUIREMENT
                        The pip install ansible requirement. Defaults to
                        "ansible"
  -r REQUIREMENTS, --requirements REQUIREMENTS
                        Path to ansible galaxy requirements file to install
                        roles from. Defaults to "build-requirements.yml"
  -p PLAYBOOK, --playbook PLAYBOOK
                        Path to playbook file to run. Defaults to "build-
                        playbook.yml"
  -e, --process-env-vars
                        Inline replace environment variables (with pattern
                        ${VAR}) in the requirements file. Backup the old file
                        to *.bak
```
