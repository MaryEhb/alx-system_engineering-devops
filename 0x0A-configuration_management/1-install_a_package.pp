# 1. Install a package

exec { 'install_flask':
  command => '/bin/pip3 install Flask==2.1.0',
  path    => '/bin',
  unless  => '/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
