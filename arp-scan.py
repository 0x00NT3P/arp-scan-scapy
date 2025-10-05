#!/usr/bin/env python
import click
from scapy.all import srp, Ether, ARP, conf
import logging
import ipaddress

logging.getLogger("scapy").setLevel(logging.CRITICAL)
conf.verb = 0

@click.group()
def arp_scan():
    pass

def valid_cidr(s: str) -> bool:
    try:
        ipaddress.ip_network(s.strip(), strict=False)
        return True
    except ValueError:
        return False

@arp_scan.command()
@click.option('--ip-range', required=True, help="ip range value, example: 192.168.0.1/24")
@click.pass_context
def arp(ctx, ip_range):
    result = valid_cidr(ip_range)
    if result:
        print("Escaneando el rango de ip: ", ip_range)
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range), timeout=0.1)

        print(f"{'IP':<15} {'MAC':<20}")
        print("-" * 35)
        for snd, rcv in ans:
            print(f"{rcv.psrc:<15} {rcv.hwsrc:<20}")
    else:
        print("Rango de red no valido.")

if __name__ == '__main__':
    arp_scan()