import paramiko
import time

ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

print('Connecting to 192.168.31.101')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname='10.10.1.10', port='22', username='cisco', password='cisco',
#                    look_for_keys=False, allow_agent=False)

router = {'hostname': '192.168.31.101', 'port': '22', 'username': 'cisco', 'password': 'cisco'}
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

#sending commands

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show ip int bri\n')
time.sleep(1)

output = shell.recv(10000)
# print(type(output))
output = output.decode('utf-8')
print(output)



if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()