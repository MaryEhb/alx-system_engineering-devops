# 0x0A. Configuration management by Puppet

## What is Puppet?

Puppet is an open-source configuration management and automation tool designed to help system administrators automate the provisioning and management of infrastructure. Puppet uses a declarative language to define the desired state of systems, and it automatically enforces and maintains that state.

## Key Concepts

### Manifests

Manifests are written in the Puppet language and describe the desired configuration of the system. They consist of resources, which represent the various aspects of system state.

### Resources

Resources are the building blocks of Puppet manifests. They represent system components such as files, packages, services, and more. Puppet ensures that the system's actual state matches the desired state defined by these resources.

## Puppet Resources

### Package Resource

The `package` resource manages the installation and removal of software packages.

```puppet
package { 'nginx':
  ensure => installed,
}
```

### File Resource

The `file` resource manages files and directories, controlling their existence, content, and permissions.

```puppet
file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => '...',
  mode    => '0644',
}
```

### Service Resource

The `service` resource manages system services, ensuring they are running or stopped.

```puppet
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
```

### Exec Resource

The `exec` resource allows the execution of arbitrary commands.

```puppet
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
  onlyif  => '/usr/bin/test ! -e /var/lib/apt/periodic/update-success-stamp',
}
```

### Class Resource

The `class` resource is used for grouping and organizing configuration code.

```puppet
class { 'web_server':
  package { 'nginx':
    ensure => installed,
  }
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}
```

## Getting Started

1. Install Puppet on the master and nodes.
2. Create Puppet manifests using the Puppet language.
3. Apply manifests using the `puppet apply` command.
4. Use Puppet modules to organize and share reusable configurations.

## Examples

For more examples and in-depth documentation, refer to the official [Puppet Documentation](https://puppet.com/docs/puppet/latest/).
