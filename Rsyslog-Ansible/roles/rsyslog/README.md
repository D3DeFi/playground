Rsyslog
=======

Configures rsyslog daemon on the system to log system and custom log messages and forward them to a centralized syslog server.

This role can configure rsyslog to act only as a client when forwarding logs to a remote server.

Requirements
------------

None

Role Variables
--------------

```yaml
rsyslog_service: rsyslog
rsyslog_package: rsyslog

# configuration directly related to rsyslog.conf
# consult the following documentation for any details:
#  /usr/share/doc/rsyslog-doc/html/rsyslog_conf.html
rsyslog_modules:
  - imuxsock  # provides support for local system logging
  - imklog    # provides kernel logging support

# Enable non-kernel facility klog messages
rsyslog_klog_permit_nonkernel_facility: on

# Use traditional timestamp format. Leave empty to enable high precision timestamps
rsyslog_action_file_default_template: RSYSLOG_TraditionalFileFormat

# Filter duplicate messages
rsyslog_repeated_msg_reduction: on

# Ownership and permissions for all log files
rsyslog_file_owner: syslog
rsyslog_file_group: adm
rsyslog_file_mode: 0640
rsyslog_dir_mode: 0755
rsyslog_umask: 0022
rsyslog_priv_drop_to_user: syslog
rsyslog_priv_drop_to_group: syslog

# Directory for rsyslog spool and state files
rsyslog_work_dir: /var/spool/rsyslog
```

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - role: rsyslog
          rsyslog_server: rsyslog.example.com
          rsyslog_server_port: 5514
            

License
-------

MIT

Author Information
------------------

@D3DeFi
