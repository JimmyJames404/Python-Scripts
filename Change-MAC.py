import subprocess


#interface = "wlan0"
#new_mac = "00:11:22:33:44:66"

interface = input("interface >")
new_mac = input("new mac >")



print("[+] Changing MAC adress for  " + interface + " to " + new_mac)

subprocess.call("ifconfig", shell=True)
subprocess.call("ifconfig "+interface+" down", shell=True)
subprocess.call("ifconfig "+interface+" hw ethe "+new_mac, shell=True)
subprocess.call("ifconfig "+interface+" up", shell=True)