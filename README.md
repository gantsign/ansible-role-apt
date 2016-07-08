Ansible Role: APT
=================

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
# Whether the cache of DEB files should be preserved or cleaned
apt_preserve_cache: false

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
     - { role: gantsign.apt, apt_preserve_cache: true }
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
