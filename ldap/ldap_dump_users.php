<?php
/**
 Purpose: Confirming you have a domain admin by dumping users within the domain on your browser (Dirty Method)
    
    Copyright (c) 2018 ~ alienwithin
    Munir Njiru <munir@alien-within.com>
 
        @version 1.0.0
        @url : https://www.alien-within.com
 **/
 
/*
Basic Settings to setup to Connect
 - Hostname - IP of the LDAP Server
 - Domain name 
 - ldap columns and alternative connection parameters
 - domain admin user and password to connect and bind with
 - base dn for users in the organization
*/
$ldap_hostname = "LDAP_Server_IP e.g 172.x.x.x";
$ldap_domain = "DOMAIN NAME e.g. EXAMPLE.COM";
$ldap_columns = NULL;
$ldap_connection = NULL;
$ldap_password = 'DOMAIN ADMIN PASSWORD';
$ldap_username = 'DOMAIN ADMIN USER'.$ldap_domain;
$ldap_base_dn = "CN=Users,DC=EXAMPLE,DC=COM";

/*
End Basic Settings to setup to Connect
*/
//------------------------------------------------------------------------------
// Connect to the LDAP server.
//------------------------------------------------------------------------------
$ldap_connection = ldap_connect($ldap_hostname);
if (FALSE === $ldap_connection){
    die("<p>Failed to connect to the LDAP server: ". $ldap_hostname ."</p>");
}

ldap_set_option($ldap_connection, LDAP_OPT_PROTOCOL_VERSION, 3) or die('Unable to set LDAP protocol version');
ldap_set_option($ldap_connection, LDAP_OPT_REFERRALS, 0); // We need this for doing an LDAP search.

if (TRUE !== ldap_bind($ldap_connection, $ldap_username, $ldap_password)){
    die('<p>Failed to bind to LDAP server.</p>');
}

//------------------------------------------------------------------------------
// Get a list of all Active Directory users.
//------------------------------------------------------------------------------

$search_filter = "(&(objectCategory=person))";
$result = ldap_search($ldap_connection, $ldap_base_dn, $search_filter);

if (FALSE !== $result){
    $entries = ldap_get_entries($ldap_connection, $result);
    if ($entries['count'] > 0){
        $odd = 0;
        foreach ($entries[0] AS $key => $value){
            if (0 === $odd%2){
                $ldap_columns[] = $key;
            }
            $odd++;
        }

        echo '<table class="data">';
        echo '<tr>';
        $header_count = 0;
        foreach ($ldap_columns AS $col_name){
            if (0 === $header_count++){
                echo '<th class="ul">';
            }else if (count($ldap_columns) === $header_count){
                echo '<th class="ur">';
            }else{
                echo '<th class="u">';
            }
            echo $col_name .'</th>';
        }
        echo '</tr>';
        for ($i = 0; $i < $entries['count']; $i++){
            echo '<tr>';
            $td_count = 0;
            foreach ($ldap_columns AS $col_name){
                if (0 === $td_count++){
                    echo '<td class="l">';
                }else{
                    echo '<td>';
                }
                if (isset($entries[$i][$col_name])){
                    $output = NULL;
                    if ('lastlogon' === $col_name || 'lastlogontimestamp' === $col_name){
                        //$output = date('D M d, Y @ H:i:s', ($entries[$i][$col_name][0] / 10000000) - 11676009600); // Windows
                        $output = date('D M d, Y @ H:i:s', ($entries[$i][$col_name][0] / 10000000) - 11644473600); // Linux
                    }else{
                        $output = $entries[$i][$col_name][0];
                    }
                    echo $output .'</td>';
                }
            }
            echo '</tr>';
        }
        echo '</table>';
    }
}
ldap_unbind($ldap_connection); // Clean up after ourselves.
?>
