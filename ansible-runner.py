#! /usr/bin/python

import fileinput
import glob
import os
import re
import shutil
import sys
import subprocess
from argparse import ArgumentParser

DEFAULT_VIRTUALENV_VERSION = '16.1.0'
DEFAULT_ANSIBLE_REQUIREMENT = 'ansible'
DEFAULT_INSTALL_DIR = '.ansible-runner'
DEFAULT_REQUIREMENTS_FILE = 'build-requirements.yml'
DEFAULT_ROLES_PATH = 'roles'
DEFAULT_PLAYBOOK_FILE = 'build-playbook.yml'

ACTION_PREFIX = '>'*5

def run_cmd(cmd):
    print "%s Running command: %s" % (ACTION_PREFIX, ' '.join(cmd))
    (stdout, stderr) = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
    print stdout

def ansible_runner():
    parser = ArgumentParser(description='Python script to install ansible in a virtual environment, install roles, and run a playbook')
    parser.add_argument('-i', '--install-dir', default=DEFAULT_INSTALL_DIR,
                      help='Installation directory for the python virtual environment. Defaults to "%s"' % DEFAULT_INSTALL_DIR )
    parser.add_argument('-c', '--clean', action='store_true',
                        help='Recreate the installation directory; Also, force the installation of roles' )
    parser.add_argument('-v', '--venv-version', default=DEFAULT_VIRTUALENV_VERSION,
                      help='Virtualenv version to use. Defaults to "%s"' % DEFAULT_VIRTUALENV_VERSION)
    parser.add_argument('-a', '--ansible-requirement', default=DEFAULT_ANSIBLE_REQUIREMENT,
                      help='The ansible requirement for the pip install. Defaults to "%s"' % DEFAULT_ANSIBLE_REQUIREMENT )
    parser.add_argument('-r', '--requirements', default=DEFAULT_REQUIREMENTS_FILE,
                      help='Path to the ansible galaxy requirements file to install roles from. Defaults to "%s"' % DEFAULT_REQUIREMENTS_FILE )
    parser.add_argument('-o', '--roles-path', default=DEFAULT_ROLES_PATH,
                      help='Path to install roles to. Defaults to "%s"' % DEFAULT_ROLES_PATH )
    parser.add_argument('-p', '--playbook', default=DEFAULT_PLAYBOOK_FILE,
                      help='Path to the playbook file to run. Defaults to "%s"' % DEFAULT_PLAYBOOK_FILE )
    parser.add_argument('-e', '--expand-env-vars', action='store_true',
                        help='Inline expand environment variables (with pattern  ${VAR}) in the requirements file. Back up the old file to *.bak' )
    args = parser.parse_args()

    if args.expand_env_vars:
        for line in fileinput.input([args.requirements], inplace=1, backup='.bak'):
            matches = re.compile(r'\${(\S*)}').findall(line.rstrip())
            for match in matches:
                line = re.sub('\${%s}' % match, os.environ[match], line.rstrip())
            print(line.rstrip())

    if args.clean and os.path.isdir(args.install_dir):
        print "%s Removing the install directory: %s" % (ACTION_PREFIX, args.install_dir)
        shutil.rmtree(args.install_dir)

    if not os.path.isdir(args.install_dir):
        print "%s Creating the install directory: %s" % (ACTION_PREFIX, args.install_dir)
        os.makedirs(args.install_dir)

    venv_archive_file = 'virtualenv-%s.tar.gz' % args.venv_version
    venv_archive_path = '%s/%s' % (args.install_dir, venv_archive_file)
    venv_archive_url = 'https://github.com/pypa/virtualenv/tarball/%s' % args.venv_version
    if not os.path.isfile(venv_archive_path):
        run_cmd(['curl', '--location', '--output', venv_archive_path, venv_archive_url])


    run_cmd(['tar', 'xvfz', venv_archive_path, '-C', args.install_dir])

    venv_unpack_dir = glob.glob('%s/pypa-virtualenv-*' % args.install_dir)[0]
    venv_dir = '%s/VE' % args.install_dir

    if not os.path.isdir(venv_dir):
        run_cmd([sys.executable, '%s/src/virtualenv.py' % venv_unpack_dir, '--system-site-packages', venv_dir])

    run_cmd(['%s/bin/pip' % venv_dir, 'install', args.ansible_requirement])

    cmd = ['%s/bin/ansible-galaxy' % venv_dir, 'install', '-r', args.requirements, '-p', args.roles_path]
    if args.clean:
        cmd.append('-f')
    run_cmd(cmd)

    run_cmd(['%s/bin/ansible-playbook' % venv_dir, args.playbook])


if __name__ == '__main__':
    ansible_runner()
