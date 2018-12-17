# ansible-runner

Python helper script to install ansible in a virtual environment, install roles, and run a playbook


## Usage

```
Usage: ansible-runner.py [options]

Options:
  -h, --help            show this help message and exit
  -r REQUIREMENTS, --requirements=REQUIREMENTS
                        Path to ansible galaxy requirements file. Defaults to
                        "build-requirements.yml"
  -p PLAYBOOK, --playbook=PLAYBOOK
                        Path to playbook file. Defaults to "build-
                        playbook.yml"
  -a ANSIBLE_REQ, --ansible-requirement=ANSIBLE_REQ
                        The pip install ansible requirement. Defaults to
                        "ansible"
  -e PYTHON_EXE, --python-exe=PYTHON_EXE
                        Path to python exe. Defaults to "python"
  -i INSTALL_DIR, --install-dir=INSTALL_DIR
                        Install dir for ansible virtual environment. Defaults
                        to ".ansible-runner"
  -v VENV_VERSION, --virtualenv-version=VENV_VERSION
                        Virtualenv version to use. Defaults to "16.1.0"
  -c, --clean           Clean the install dir, if it exists.
```

## Example
