from netmiko import ConnectHandler

with open('devices.txt') as f:
    devices = f.read().splitlines()

for ip in devices:

    cisco_device = {
           'device_type': 'cisco_nxos',
           'host': ip,
           'username': 'cisco',
           'password': 'cisco',
           'port': 22,             # optional, default 22
           'secret': 'cisco',      # this is the enable password
           'verbose': True         # optional, default False
           }
    connection = ConnectHandler(**cisco_device)
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]
    print(f"Start to save config of {hostname}")
    connection.send_command('wr')
    print("save config done")


    print('Closing connection')
    connection.disconnect()