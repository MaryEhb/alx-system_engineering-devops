# 2. Execute a command

exec { 'killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
}
