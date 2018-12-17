#! /usr/bin/python

import glob
import os
import shutil
import sys
from optparse import OptionParser
from subprocess import call

DEFAULT_VIRTUALENV_VERSION = '16.1.0'
DEFAULT_ANSIBLE_REQ = 'ansible'

def run():
    parser = OptionParser()
    parser.add_option('-i', '--install-dir', dest='install_dir', default='.ansible-runner',
                      help='Install dir for ansible virtual environment. Defaults to ".ansible-runner"' )
    parser.add_option('-c', '--clean', dest='clean', action='store_true',
                      help='Clean the install dir, if it exists.' )
    parser.add_option('-v', '--virtualenv-version', dest='venv_version', default=DEFAULT_VIRTUALENV_VERSION,
                      help='Virtualenv version to use. Defaults to "%s"' % DEFAULT_VIRTUALENV_VERSION)
    parser.add_option('-a', '--ansible-requirement', dest='ansible_req',  default=DEFAULT_ANSIBLE_REQ,
                      help='The pip install ansible requirement. Defaults to "%s"' % DEFAULT_ANSIBLE_REQ )
    parser.add_option('-r', '--requirements', dest='requirements', default='build-requirements.yml',
                      help='Path to ansible galaxy requirements to install roles from. Defaults to "build-requirements.yml"' )
    parser.add_option('-p', '--playbook', dest='playbook', default='build-playbook.yml',
                      help='Path to playbook file to run. Defaults to "build-playbook.yml"' )
    (options, args) = parser.parse_args()

    if options.clean and os.path.isdir(options.install_dir):
        shutil.rmtree(options.install_dir)

    if not os.path.isdir(options.install_dir):
        os.makedirs(options.install_dir)

    venv_archive_file = 'virtualenv-%s.tar.gz' % options.venv_version
    venv_archive_path = '%s/%s' % (options.install_dir, venv_archive_file)
    venv_archive_url = 'https://github.com/pypa/virtualenv/tarball/%s' % options.venv_version
    if not os.path.isfile(venv_archive_path):
        call(['curl', '--location', '--output', venv_archive_path, venv_archive_url])

    call(['tar', 'xvfz', venv_archive_path, '-C', options.install_dir])

    venv_unpack_dir = glob.glob('%s/pypa-virtualenv-*' % options.install_dir)[0]
    venv_dir = '%s/VE' % options.install_dir

    if not os.path.isdir(venv_dir):
        call([sys.executable, '%s/src/virtualenv.py' % venv_unpack_dir, venv_dir])

    call(['%s/bin/pip' % venv_dir, 'install', options.ansible_req])
    call(['%s/bin/ansible-galaxy' % venv_dir, 'install', '-r', options.requirements])
    call(['%s/bin/ansible-playbook' % venv_dir, options.playbook])


if __name__ == '__main__':
    run()
