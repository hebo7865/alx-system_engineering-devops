# kills a process

exec { 'pkill':
  command   => '/usr/bin/pkill killmenow',
  provider  => 'shell',
  returns   => [0, 1],
}
