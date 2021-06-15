import os
import json
from pathlib import Path

datos = {}
datos['Palo Alto Networks'] = []
datos['Cisco'] = []
datos['Amazon'] = []


Palo_Alto_Networks = [{
    'RED LAN':[ 'Firewall NG','IPS','Cliente de Seguridad Movil'],
    'CLOUD':[ 'Soluciones SD-WAN','Seguridad en la Nube','Servicios de Acceso Seguro'],
    'SOC':[ 'Corteza XDR','WildFire','Recopilacion de datos de seguridad']}]

Cisco = [{
    'RED LAN':[ 'Firewall', 'Switches de acceso de clientes', 'Routers WAN', 'Controlador de LAN inalambrico'],
    'CLOUD':[ 'Nube de ACI','CSR 1000v','Cloudlock','AppDynamics,'],
    'SOC':[ 'Identity Services Engine', 'Firewalls Firepower', 'Stealthwatch']}]

Amazon = [{
    'RED LAN':[ 'AWS Outposts', 'Amazon EC2 ', 'Firewall ', 'VPN IPsec'],
    'CLOUD':[ 'Amazon CloudSearch','Seguridad en la Nube','Amazon Elasticsearch Service'],
    'SOC':[ ' AWS Artifact', 'Amazon DocumentDB', 'AWS IoT Core', 'AWS DataSync']}]

datos['Palo Alto Networks'].append(Palo_Alto_Networks)
datos['Cisco'].append(Cisco)
datos['Amazon'].append(Amazon)

diccionario=[]


def menu():
    print()
    print("1. Agregar")
    print("2. Guardar diccionario en .json")
    print("3. Visualizar diccionario .json")
    print("0. Salir")

continuar = True
while(continuar):
    menu()
    opc = input("Digite su opcion: ")

    if opc == "1":
        print()
        print("Agregar datos")
        diccionario = []
        diccionario.append(input("Ingrese tecnologia: "))
        diccionario.append(input("Ingrese el servicio: "))
        diccionario.append(input("Ingrese descripcion: "))
        equipos.append(diccionario)
        datos = json.dumps(equipos)
        
        f=open("diccionario.json", "w")
        f.write(datos)
        f.close()
        
        input("Se agrego, presione enter para continuar")
        print()
        
    elif opc == "2":
        print()
        with open('diccionario.json', 'w') as f:
            json.dump(datos, f, indent=4, sort_keys=True)
        input("Presione enter para continuar")
        print()
        
    elif opc == "3":
        ubicacion = Path("diccionario.json")
        if ubicacion.exists():
            with open('diccionario.json', 'r') as f:
                datos_equipos = json.load(f)
            print()
            print(datos_equipos)
            print()
            input("Presione enter para continuar")
            print()
        else:
            print()
            print("!Primero debes guardar el diccionario¡")
            print()

        input("Presione enter para continuar")

    elif opc == "0":
        continuar = False
        
    else:
        print("Opcion no valida")
        input("Presione enter para continuar")
        
        
    
