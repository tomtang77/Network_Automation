import json
from napalm import get_network_driver

driver = get_network_driver('nxos')
optional_args = {'secret': 'cisco'} # cisco is the enable password
nxos = driver('192.168.31.102', 'cisco', 'cisco', optional_args=optional_args)
nxos.open()
#start your code

output = nxos.get_interfaces_ip()
for item in output:
    print(item)

dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

# write the output into a file
# with open('arp.txt', w) as f:
#     f.write(dump)

#end your code
nxos.close()