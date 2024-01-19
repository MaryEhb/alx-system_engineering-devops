# 1. Install a package

exec { 'install_python3_pip':
  command => '/usr/bin/apt-get install -y python3-pip',
  path    => '/usr/bin',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Exec['install_python3_pip'],
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.1.1',
  path    => '/usr/bin',
  unless  => '/usr/bin/pip3 show Werkzeug | grep -q "Version: 2.1.1"',
  require => Exec['install_python3_pip'],
}
