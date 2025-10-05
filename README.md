# Escáner ARP

Esta es una herramienta simple de escaneo de red construida con Python que realiza escaneos ARP (Address Resolution Protocol) en un rango de IP específico para descubrir hosts activos en una red.

## Características

- Realiza escaneos ARP en un rango de IP específico
- Valida entradas en notación CIDR
- Muestra los hosts descubiertos con sus direcciones IP y MAC
- Interfaz de línea de comandos utilizando el framework Click

## Requisitos

- Python 3.x
- Scapy
- Click
- Privilegios de root/administrador (requeridos para el escaneo ARP)

Puedes instalar los paquetes requeridos usando:

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar un escaneo ARP en una red:

```bash
python arp-scan.py arp --ip-range <RANGO_IP>
```

Ejemplo:

```bash
python arp-scan.py arp --ip-range 192.168.0.1/24
```

La salida mostrará una tabla con:

- Direcciones IP de los hosts descubiertos
- Direcciones MAC de los hosts descubiertos

## Ejemplo de Salida

```
Escaneando el rango de ip: 192.168.0.1/24
IP              MAC
-----------------------------------
192.168.0.1     00:11:22:33:44:55
192.168.0.100   aa:bb:cc:dd:ee:ff
```

## Notas

- La herramienta requiere privilegios de root/administrador para realizar escaneos ARP
- El tiempo de espera predeterminado para las respuestas ARP está configurado en 0.1 segundos
- La herramienta utiliza peticiones ARP de broadcast para descubrir hosts
- La notación CIDR inválida será rechazada con un mensaje de error
