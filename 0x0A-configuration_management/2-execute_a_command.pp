# kills a process

exec { 'pkill killmenow':
  command   => '/usr/bin:/usr/sbin:/bin',
  provider  => 'shell',
  returns   => [0, 1],
}
