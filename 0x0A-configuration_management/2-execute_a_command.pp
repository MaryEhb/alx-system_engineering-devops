# 2. Execute a command

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
}
