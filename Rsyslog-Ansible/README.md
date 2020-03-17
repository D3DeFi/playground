Rsyslog-Ansible
===============

is a simple project demonstrating how to configure rsyslog service via Ansible roles.

Installation
------------

    pip install ansible

Configuration
-------------

For all configuration options of the rsyslog role, consult roles/rsyslog/README.md

To enable log forwarding to a remote syslog server define:

    rsyslog_remote_server: syslog.example.com
    rsyslog_remote_port: 5514  # default 514

Execution
---------

    echo MYHOST > hosts  # or setup proper ansible inventory
    ansible-playbook site.yml
