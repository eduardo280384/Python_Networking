from netmiko import ConnectHandler
from getpass import getpass
router_cisco_7200 = {
    "device_type": "cisco_ios",
    "host": "192.168.9.228",
    "username": "admin",
    "password": "admin",
    "port":22,
    "secret": "admin",
}
command = 'show ip interface brief'
with ConnectHandler(**router_cisco_7200) as net_connect:
    output = net_connect.send_command(command)
    print()
    print(output)
    print()