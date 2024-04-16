exec { 'update_nginx_config':
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/',
}

exec { 'restart_nginx':
    command => '/etc/init.d/nginx restart',
    path    => '/etc/init.d',
}
