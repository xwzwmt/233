# encoding=utf-8
#!/usr/bin/env python
"""cap
A tool for network class
Usage:
    cap -s <net>
    cap -d <target1> <target2>
    cap -l

Options:
    -s --scan_host    Scan all host in the net
    -d --do_arp       Do arp
    -l --look         Look picture
"""

from docopt import docopt
from tools import scanHost
from tools import do_arp
from tools import look
if __name__=='__main__':
    opt=docopt(__doc__,version='1.0')

    if opt['--scan_host']:
        net =opt['<net>']
        print 'Scan %s ......' %net
        scanHost(net)
    elif opt['--do_arp']:
        target1=opt['<target1>']
        target2=opt['<target2>']
        do_arp(target1,target2)
    elif opt['--look']:
        look()