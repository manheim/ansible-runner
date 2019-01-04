# ansible-runner.py

Python script to install ansible in a virtual environment, install roles, and run a playbook


## Usage

```
usage: ansible-runner.py [-h] [-i INSTALL_DIR] [-c] [-v VENV_VERSION]
                         [-a ANSIBLE_REQUIREMENT] [-r REQUIREMENTS]
                         [-o ROLES_PATH] [-p PLAYBOOK] [-e]

Python script to install ansible in a virtual environment, install roles, and
run a playbook

optional arguments:
  -h, --help            show this help message and exit
  -i INSTALL_DIR, --install-dir INSTALL_DIR
                        Installation directory for the python virtual
                        environment. Defaults to ".ansible-runner"
  -c, --clean           Recreate the installation directory; Also, force the
                        installation of roles
  -v VENV_VERSION, --venv-version VENV_VERSION
                        Virtualenv version to use. Defaults to "16.1.0"
  -a ANSIBLE_REQUIREMENT, --ansible-requirement ANSIBLE_REQUIREMENT
                        The ansible requirement for the pip install. Defaults
                        to "ansible"
  -r REQUIREMENTS, --requirements REQUIREMENTS
                        Path to the ansible galaxy requirements file to
                        install roles from. Defaults to "build-
                        requirements.yml"
  -o ROLES_PATH, --roles-path ROLES_PATH
                        Path to install roles to. Defaults to "roles"
  -p PLAYBOOK, --playbook PLAYBOOK
                        Path to the playbook file to run. Defaults to "build-
                        playbook.yml"
  -e, --expand-env-vars
                        Inline expand environment variables (with pattern
                        ${VAR}) in the requirements file. Back up the old file
                        to *.bak
```
