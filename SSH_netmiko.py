# from netmiko import Netmiko
#
# connection = Netmiko(host="10.10.1.10", port="22", username="cisco", password="cisco", device_type="cisco_ios")

from netmiko import ConnectHandler
cisco_device = {
    "device_type": "cisco_ios",
    "host": "192.168.31.101",
    "username": "cisco",
    "password": "cisco",
    "port": "22",
    "secret": "cisco",
    "verbose": True
}

connection = ConnectHandler(**cisco_device)

output = connection.send_command("show ver")
print(output)

print("Closing connection")
connection.disconnect()