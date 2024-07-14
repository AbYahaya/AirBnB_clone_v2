# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the necessary directories are created
file { '/data/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
  recurse => true,
}

file { '/data/web_static/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/shared/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
<head>
<title>Test Page</title>
</head>
<body>
<h1>This is a test page</h1>
</body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create/recreate the symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Ensure the Nginx configuration file contains the required alias directive
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
