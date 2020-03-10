Docker
=========

Simple role to setup docker on a Ubuntu system with syslog logging

Requirements
------------

None

Role Variables
--------------

    # log driver to use with docker service
    # see https://docs.docker.com/config/containers/logging/configure/
    docker_log_driver: syslog

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - docker

License
-------

MIT

Author Information
------------------

@D3DeFi
