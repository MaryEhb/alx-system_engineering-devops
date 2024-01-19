# 1. Install a package

exec { 'flask':
    command => 'pip3 install flask==2.1.0',
    creates => '/usr/local/bin/flask'
    require => Package['python3-pip'],
}
