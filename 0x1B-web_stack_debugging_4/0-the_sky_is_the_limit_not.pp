# 0x1B. Web stack debugging #4


exec { 'fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
