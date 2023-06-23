from scapy.all import *
from collections import namedtuple
import pyfiglet

Answer = namedtuple('Answer', 'ip mac')

def arp_scan(ip):
    request = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip)
    answer, _ = srp(request, timeout=0.5, retry=1)
    results = []
    for _, packet in answer:
        results.append(Answer(packet.psrc, packet.hwsrc))
    return results

if __name__ == '__main__':
    ascii_banner = pyfiglet.figlet_format("IP MAC Scanner")
    print(ascii_banner)
    print("-" * 100)
    all_answers =[]
    gateway = '' # you need your gateway(ipconfig / ifconfig)
    for corrent_ip in range(20):
        all_answers.append(arp_scan(f'{gateway}.{corrent_ip}'))
    for answer in all_answers:
        if len(answer) > 0:
            for packet in answer:
                print(f'Host {packet.ip} is up with MAC: {packet.mac}')