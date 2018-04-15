Ansible Role: APT
=================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-apt.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-apt)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.apt-blue.svg)](https://galaxy.ansible.com/gantsign/apt)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-apt/master/LICENSE)

Role to configure the APT package manager. Currently limited to controlling the
properties that affect the cleaning of the DEB files (typically by the APT cron
job). The DEB files are removed to save on disk space but if you're using
Vagrant (with the vagrant-cachier plugin) you may want to keep the DEB files to
speed up VM rebuilds.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The filename for the apt config
apt_config_filename: '80-vagrant'

# Whether the cache of DEB files should be preserved or cleaned
apt_preserve_cache: no

# Max age (in days) of DEB files to keep when cleaning cache
apt_archives_maxage: null

# Min age (in days) of DEB files to keep when cleaning cache
apt_archives_minage: null

# Max size (in MB) of DEB files to keep when cleaning cache
apt_archives_maxsize: null
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.apt
      apt_preserve_cache: yes
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
