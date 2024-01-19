# 2. Execute a command

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  provider    => 'shell',
}
