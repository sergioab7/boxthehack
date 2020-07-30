#!/usr/bin/python3
#coding:utf-8

#Autor: xaxxjs (https://sergioab7.github.io/index.html)

#Thanks to (sw1tch-bl4d3) (https://gitlab.com/sw1tchbl4d3) for the API

from bs4 import BeautifulSoup

from challenges import challenges
from machines import machines
from social import social

import re

from htbapi.core import getRequest, rawPostSSL


from beautifultable import BeautifulTable
from colorama import Fore, Back, Style
import signal
from time import sleep
import signal
import json
import warnings
import os, sys
warnings.filterwarnings("ignore")

def signal_handler(key,frame):
    print(Fore.YELLOW + "\n[*]" + Fore.RESET + "[!] Saliendo... \n")
    print(Style.RESET_ALL)
    sys.exit(1)

signal=signal.signal(signal.SIGINT,signal_handler)

#api="P884J96j657M7DlgJElLgJPriuSlfeNa0IgGcoyqKBHIENfP2qoxBMWXPKdm"

banner=Fore.GREEN + """
       __               __  __         __               __  
      / /_  ____  _  __/ /_/ /_  ___  / /_  ____ ______/ /__
     / __ \/ __ \| |/_/ __/ __ \/ _ \/ __ \/ __ `/ ___/ //_/
    / /_/ / /_/ />  </ /_/ / / /  __/ / / / /_/ / /__/ ,<   
   /_.___/\____/_/|_|\__/_/ /_/\___/_/ /_/\__,_/\___/_/|_|  
                                           """+Fore.RESET+"""By:xaxxjs 
                                           Web: https://sergioab7.github.io/            
"""
os.system("clear")
print(banner)


def api():
    f=open("api.txt", "w")
    comando=input(Fore.BLUE + "INSERTA TU API>>" + Fore.RESET)
    while(len(comando)<50):
         comando=input(Fore.BLUE + "INSERTA TU API>>" + Fore.RESET)
    print(Fore.YELLOW + "\n\t\t[API AGREGADA CON ÉXITO]" + Fore.RESET)
    print(Fore.YELLOW + "\n\t\tReinicia el servicio para que se apliquen los cambios\n\n" + Fore.RESET)
    f.write(comando)
    f.close()
    sys.exit()

if(os.path.isfile("api.txt")):
    with open("api.txt", "r") as app:
        API = app.read()
    app.close()
else:
    api()

os.system("clear")
print(banner)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def comandos_general():
    print("""
        """+ bcolors.FAIL +"[+]"+bcolors.ENDC + """ Maquina
        """+ bcolors.FAIL +"[+]"+bcolors.ENDC + """ Social
        """+ bcolors.FAIL +"[+]"+bcolors.ENDC + """ Challenges

        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Clear 
        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Exit 
        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Help
    """)

comandos_general()



def comandos_maquina():
    print("""
        """+ bcolors.HEADER +"\n\t\t[INFORMACIÓN]" + bcolors.ENDC + """ 
        """+ bcolors.FAIL +"[1]"+bcolors.ENDC + """ Mostrar todas las máquinas. 
        """+ bcolors.FAIL +"[2]"+bcolors.ENDC + """ Mostrar todas las máquinas activas.
        """+ bcolors.FAIL +"[3]"+bcolors.ENDC + """ Mostrar todas las máquinas retiradas.
        """+ bcolors.HEADER +"\n\t\t[INTERACCIÓN]" + bcolors.ENDC + """ 
        """+ bcolors.FAIL +"[4]"+bcolors.ENDC + """ Inserta la flag (user/root).
        """+ bcolors.FAIL +"[5]"+bcolors.ENDC + """ Resetea la máquina.
        """+ bcolors.FAIL +"[6]"+bcolors.ENDC + """ Asigna una máquina.
        """+ bcolors.FAIL +"[7]"+bcolors.ENDC + """ Extiende el tiempo de la máquina.
        """+ bcolors.FAIL +"[8]"+bcolors.ENDC + """ Para la máquina.

        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Back
        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Clear 
        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Help
    """)

def mostrar_todas_las_maquinas():
    try:
        table=BeautifulTable()
        table.set_style(BeautifulTable.STYLE_GRID)
        test=table.columns.header=[Fore.CYAN+"MÁQUINA"+Fore.RESET,Fore.CYAN+"S.O"+Fore.RESET,Fore.CYAN+"IP"+Fore.RESET,Fore.CYAN+"Puntos"+Fore.RESET,Fore.CYAN+"USER OWN"+Fore.RESET,Fore.CYAN+"ROOT OWN"+Fore.RESET,Fore.CYAN+"RATING"+Fore.RESET,Fore.CYAN+"BY"+Fore.RESET]
        for i in machines.getAllMachines(API):
            table.append_row([f"{i['name']}", f"{i['os']}", f"{i['ip']}", f"{i['points']}", f"{i['user_owns']}", f"{i['root_owns']}", f"{i['rating']}", f"{i['maker']['name']}"])
        for i in test:
            table.left_padding_widths[i]=1
            table.right_padding_widths[i]=1
        print(table)
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)

def mostrando_maquinas_activas():
    try:
        activemachines = []
        allmachines = machines.getAllMachines(API)
        for machine in allmachines:
            if machine["retired"] == False:
                activemachines.append(machine)
        table=BeautifulTable()
        table.set_style(BeautifulTable.STYLE_GRID)
        test=table.columns.header=[Fore.CYAN+"MÁQUINA"+Fore.RESET,Fore.CYAN+"S.O"+Fore.RESET,Fore.CYAN+"IP"+Fore.RESET,Fore.CYAN+"Puntos"+Fore.RESET,Fore.CYAN+"USER OWN"+Fore.RESET,Fore.CYAN+"ROOT OWN"+Fore.RESET,Fore.CYAN+"RATING"+Fore.RESET,Fore.CYAN+"BY"+Fore.RESET]
        for i in activemachines:
            table.append_row([f"{i['name']}", f"{i['os']}", f"{i['ip']}", f"{i['points']}", f"{i['user_owns']}", f"{i['root_owns']}", f"{i['rating']}", f"{i['maker']['name']}"])
        for i in test:
            table.left_padding_widths[i]=1
            table.right_padding_widths[i]=1
        print(table)
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)
       

def mostrando_maquinas_retiradas():
    try:
        retiredmachines = []
        allmachines = machines.getAllMachines(API)
        for machine in allmachines:
            if machine["retired"] == True:
                retiredmachines.append(machine)
        table=BeautifulTable()
        table.set_style(BeautifulTable.STYLE_GRID)
        test=table.columns.header=[Fore.CYAN+"MÁQUINA"+Fore.RESET,Fore.CYAN+"S.O"+Fore.RESET,Fore.CYAN+"IP"+Fore.RESET,Fore.CYAN+"Puntos"+Fore.RESET,Fore.CYAN+"USER OWN"+Fore.RESET,Fore.CYAN+"ROOT OWN"+Fore.RESET,Fore.CYAN+"RATING"+Fore.RESET,Fore.CYAN+"BY"+Fore.RESET]
        for i in retiredmachines:
            table.append_row([f"{i['name']}", f"{i['os']}", f"{i['ip']}", f"{i['points']}", f"{i['user_owns']}", f"{i['root_owns']}", f"{i['rating']}", f"{i['maker']['name']}"])
        for i in test:
            table.left_padding_widths[i]=1
            table.right_padding_widths[i]=1
        print(table)
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)

def conversor_id(maquina):
    try:
        maquina = maquina.lower()
        maquina = maquina.capitalize()
        maquina_id=""
        for i in machines.getAllMachines(API):
            if(i['name']==maquina):
                maquina_id = i['id']
        return maquina_id
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)

def inserta_flag(maquina_htb):
    try:
        machine_id=conversor_id(maquina_htb)
        flag=input(Fore.YELLOW + "\t[+]"+ Fore.RESET + "Inserta la flag(user/root) >>")
        dificultad=int(input(Fore.YELLOW + "\t[+]"+Fore.RESET + "Inserta la dificultad (1-10) >>"))
        resultado=machines.ownMachine(machine_id, API, flag,dificultad)
        if(resultado=="success"):
            print(Fore.GREEN + "\n\t[+] SUCCESS!" +Fore.RESET)
        elif(resultado=="flag_invalid"):
            print(Fore.RED + "\n\t[+] FLAG INVÁLIDA" +Fore.RESET)
        elif(resultado=="failed"):
            print(Fore.RED + "\n\t[+] SUCCESS! " +Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)

def resetea_maquina(maquina_htb):
    try:
        machine_id=conversor_id(maquina_htb)
        resultado=machines.resetMachine(machine_id, API)
        print(Fore.GREEN + "[+] Máquina reseteada con éxito."+Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)
    
def asignar_maquina(maquina_htb):
    try:
        machine_id=conversor_id(maquina_htb)
        resultado=machines.assignMachine(machine_id, API)
        if(resultado=="success"):
            print(Fore.GREEN + "\n\t[+] MAQUINA ASIGNADA!" +Fore.RESET)
        elif(resultado=="already_have_machiine"):
            print(Fore.RED + "\n\t[+] YA TIENES LA MAQUINA EN USO!" +Fore.RESET)
        elif(resultado=="no_vip"):
            print(Fore.RED + "\n\t[+] MAQUINA INCORRECTA!" +Fore.RESET)
        elif(resultado=="failed"):
            print(Fore.GREEN + "\n\t[+] MAQUINA ASIGNADA!" +Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)

def parar_maquina(maquina_htb):
    machine_id=conversor_id(maquina_htb)
    response=machines.stopMachine(machine_id,API)
    print(Fore.GREEN + "\n\t[+] SUCCESS!" +Fore.RESET)

def extender_tiempo_maquina(maquina_htb):
    machine_id=conversor_id(maquina_htb)
    response=machines.extendMachine(machine_id, API)
    print(Fore.GREEN + "\n\t[+] SUCCESS!" +Fore.RESET)




def maquina():
    comandos_maquina()
    while True:
        try:
            comando=input(bcolors.UNDERLINE + "boxthehack" + bcolors.ENDC + "/(MAQUINA)> ")
            comando=comando.lower()
            if(comando=="help"):
                comandos_maquina()
            elif(comando=="back"):
                break
            elif(comando=="1"):
                print("[+]Mostrando todas las máquinas...")
                sleep(1)
                mostrar_todas_las_maquinas()
            elif(comando=="2"):
                print("[+]Mostrando todas las máquinas activas...")
                sleep(1)
                mostrando_maquinas_activas()
            elif(comando=="3"):
                print("[+]Mostrando todas las máquinas retiradas...")
                sleep(1)
                mostrando_maquinas_retiradas()
            elif(comando=="4"):
                print(Fore.GREEN + "[!]"+Fore.RESET+" INSERTA FLAG")
                sleep(0.5)
                nombre_maquina=input(Fore.YELLOW + "\n\t[+]"+ Fore.RESET + "Inserta el nombre de la máquina>>")
                inserta_flag(nombre_maquina)
            elif(comando=="5"):
                print(Fore.GREEN + "[!]"+Fore.RESET+" RESETEA MAQUINA")
                sleep(1)
                nombre_maquina=input(Fore.YELLOW + "\n\t[+]"+ Fore.RESET + "Inserta el nombre de la máquina>>")
                resetea_maquina(nombre_maquina)
            elif(comando=="6"):
                print(Fore.GREEN + "[!]"+Fore.RESET+" ASIGNAR MAQUINA")
                sleep(1)
                nombre_maquina=input(Fore.YELLOW + "\n\t[+]"+ Fore.RESET + "Inserta el nombre de la máquina>>")
                asignar_maquina(nombre_maquina)
            elif(comando=="7"):
                print(Fore.GREEN + "[!]"+Fore.RESET+" EXTIENDE EL TIEMPO DE LA MAQUINA")
                sleep(1)
                nombre_maquina=input(Fore.YELLOW + "\n\t[+]"+ Fore.RESET + "Inserta el nombre de la máquina>>")
                extender_tiempo_maquina(nombre_maquina)
            elif(comando=="8"):
                print(Fore.GREEN + "[!]"+Fore.RESET+" PARAR MAQUINA")
                sleep(1)
                nombre_maquina=input(Fore.YELLOW + "\n\t[+]"+ Fore.RESET + "Inserta el nombre de la máquina>>")
                parar_maquina(nombre_maquina)
            elif(comando=="clear"):
                os.system("clear")
                print(banner)
            else:
                print(Fore.RED + "[-] " +Fore.RESET + "Error, no existe el comando")
        except Exception as e:
            print("Error: %s"%(e))

def comandos_social():
    print("""
        """+ bcolors.HEADER +"\n\t\t[INFORMACIÓN]" + bcolors.ENDC + """ 
        """+ bcolors.FAIL +"[1]"+bcolors.ENDC + """ Mostrar último mensaje de la ShoutBox. 
        """+ bcolors.FAIL +"[2]"+bcolors.ENDC + """ Mostrar todas tus conversaciones.
        """+ bcolors.HEADER +"\n\t\t[INTERACCIÓN]" + bcolors.ENDC + """ 
        """+ bcolors.FAIL +"[3]"+bcolors.ENDC + """ Enviar mensaje a la ShoutBox.
        """+ bcolors.FAIL +"[4]"+bcolors.ENDC + """ Inicia conversación con un destinatario.
        """+ bcolors.FAIL +"[5]"+bcolors.ENDC + """ Envía mensaje a una conversación ya iniciada.

        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Back
        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Clear 
        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Help
    """)

def mostrar_ultimo_mensaje():
    try:
        response = rawPostSSL(f"/shouts/get/initial/html/1", "", API, "", "}").decode()
        if '"success":"0"' in response:
            return "failed"
        response = response[response.find('{"success":"1"'):]
        bs=BeautifulSoup(response, "lxml")
        ref=bs.find_all('a')
        span=bs.find_all('span')
        for r in ref:
            print(r.contents[0])
        
        for i in span:
            print(i.contents[0])


    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)

def todas_conversaciones():
    try:
        response = rawPostSSL("/conversations/list/", "", API, "", '"}]').decode()
        response = response[response.find('[{"id":'):]
        jsondata = json.loads(response)
        for i in jsondata:
            print(Fore.YELLOW+"\n\t\t%s: %s -> %s"%(i['id'],i['usernames'], i['lastmessage'])+Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)

def enviar_mensaje_shout():
    try:
        msg=input("\n\t[+] Escribe el mensaje que quieras enviar >>")
        response = rawPostSSL("/shouts/new/", f"text={msg}", API, "x-www-form-urlencoded", "")
        print(Fore.GREEN + "[+] Mensaje enviado" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)

def inicia_conversacion(destinatario):
    try:
        msg=input("\n\t[+] Escribe el mensaje que quieras enviar >>")
        response =  rawPostSSL("/conversations/new/", f"recipients%5B%5D={destinatario}&message={msg}", API, "x-www-form-urlencoded", "")
        print(Fore.GREEN + "[+] Mensaje enviado" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)

def conversacion_iniciada():
    try:
        response = rawPostSSL("/conversations/list/", "", API, "", '"}]').decode()
        response = response[response.find('[{"id":'):]
        jsondata = json.loads(response)
        for i in jsondata:
            print(Fore.YELLOW+"\n\t\t%s: %s -> %s"%(i['id'],i['usernames'], i['lastmessage'])+Fore.RESET)

        conversationid=int(input("\n\t[+]Ingresa el 'ID' del usuario>> "))
        msg=input("\n\t[+] Escribe el mensaje que quieras enviar >>")
        
        response = rawPostSSL(f"/conversations/send/{conversationid}/", f"id={conversationid}&message={msg}", API, "x-www-form-urlencoded", "")
        print(Fore.GREEN + "[+] Mensaje enviado" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)


def social():
    comandos_social()
    while True:
        try:
            comando=input(bcolors.UNDERLINE + "boxthehack" + bcolors.ENDC + "/(SOCIAL)> ")
            comando=comando.lower()
            if(comando=="help"):
                comandos_maquina()
            elif(comando=="back"):
                break
            elif(comando=="1"):
                print("[+] Mostrando ultimo mensaje..")
                sleep(1.5)
                mostrar_ultimo_mensaje()
            elif(comando=="2"):
                print("[+] Mostrando todas las conversaciones..")
                sleep(1.5)
                todas_conversaciones()
            elif(comando=="3"):
                enviar_mensaje_shout()
            elif(comando=="4"):
                destinatario=input(Fore.YELLOW + "\t[+]"+ Fore.RESET + " Introduce destinatario>>")
                inicia_conversacion(destinatario)
            elif(comando=="5"):
                conversacion_iniciada()
            elif(comando=="clear"):
                os.system("clear")
                print(banner)
            else:
                print(Fore.RED + "[-] " +Fore.RESET + "Error, no existe el comando")
        except Exception as e:
            print("Error: %s"%(e))


def comandos_challenge():
    print("""
        """+ bcolors.FAIL +"[1]"+bcolors.ENDC + """ Flag del challenge [NO OPERATIVO]. 

        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Back
        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Clear
        """+ bcolors.WARNING +"[+]"+bcolors.ENDC + """ Help
    """)

def comprobar_flag(flag):
    try:
        #MODIFICAR
        #MODIFICAR
        #MODIFICAR
        response =  rawPostSSL("/challenges/own/", f'challenge_id={challengeid}&flag={flag}&difficulty={difficulty * 10}', API, "x-www-form-urlencoded", "")
        if '"success":"1"'.encode() in response:
            return "success"
        elif "Incorrect flag".encode() in response:
            return "flag_invalid"
        else:
            return "failed"
    except Exception as e:
        print(Fore.RED + "Error: %s"%(e) + Fore.RESET)

def challenges():
    comandos_challenge()
    while True:
        try:
            comando=input(bcolors.UNDERLINE + "boxthehack" + bcolors.ENDC + "/(CHALLENGES)> ")
            comando=comando.lower()
            if(comando=="1"):
                #flag=input("[+] Introduce la FLAG >>")
                break
            elif(comando=="back"):
                break 
            elif(comando=="clear"):
                os.system("clear")
                print(banner)
            elif(comando=="help"):
                comandos_challenge()
            else:
                print(Fore.RED + "[-] " +Fore.RESET + "Error, no existe el comando")
        except Exception as e:
            print("Error: %s"%(e))



while True:
    comando=input(bcolors.UNDERLINE + "boxthehack" + bcolors.ENDC + " > ")
    comando=comando.lower()
    try:
        if(comando=="maquina"):
            maquina()
        elif(comando=="social"):
            social()
        elif(comando=="challenges"):
            challenges()
        elif(comando=="help"):
            comandos_general()
        elif(comando=="clear"):
            os.system("clear")
            print(banner)
        elif(comando=="exit"):
            sys.exit(1)
        else:
            print(Fore.RED + "[-] " +Fore.RESET + "Error, no existe el comando")
    except Exception as e:
        print("Error: %s"%(e))
