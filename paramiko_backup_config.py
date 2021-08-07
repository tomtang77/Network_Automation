import paramiko
import time

def connect(device_ip, device_port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting to {device_ip}")
    ssh_client.connect(hostname=device_ip, port=device_port, username=username, password=password,
                       look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

if __name__ == '__main__':
    router1 = {'device_ip': '192.168.31.101', 'device_port': '22', 'username': 'cisco', 'password': 'cisco'}
    router2 = {'device_ip': '192.168.31.102', 'device_port': '22', 'username': 'cisco', 'password': 'cisco'}
    router3 = {'device_ip': '192.168.31.103', 'device_port': '22', 'username': 'cisco', 'password': 'cisco'}

    routers = [router1, router2, router3]

    for router in routers:

        client = connect(**router)
        shell = get_shell(client)

        send_command(shell, 'enable')
        send_command(shell, 'cisco')
        send_command(shell, 'terminal length 0')
        send_command(shell, 'show run')

        output = show(shell)
        # print(output)
        output_list = output.splitlines()
        output_list = output_list[20:-1]
        # print(output_list)
        output = '\n'.join(output_list)

        from datetime import datetime
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute

        file_name = f'{router["device_ip"]}, {year}-{month}-{day}-{hour}-{minute}.txt'
        print(file_name)

        with open(file_name, 'w') as f:
            f.write(output)

        close(client)