# "phpp" to "php" /var/www/html/wp-settings.php

exec { 'fix':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/ust/local/bin/:bin/'
}
