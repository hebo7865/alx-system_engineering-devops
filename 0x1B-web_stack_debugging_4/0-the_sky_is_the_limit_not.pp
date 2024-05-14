# fix problem of to many requests

exec { 'fix-nginx':
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
}



exec { 'nginx':
  command => '/usr/sbin/service nginx restart',
  require => Exec['fix-nginx'],
}
