# Execute a command

exec {'killmenow':
  command => 'pkill killmenow',
  path    => '/bin/'
}
