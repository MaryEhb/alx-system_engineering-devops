# 1. Install a package

exec { 'flask':
    command => 'pip3 install flask==2.1.0',
    require => Package['python3-pip'],
}
