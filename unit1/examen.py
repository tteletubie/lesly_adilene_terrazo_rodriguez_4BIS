class DataCenter:
    def __init__(self, region_name):
        self.region_name = region_name
        self.servers = []
        
    def register_server(self, server):
        self.servers.append(server)
    

class Server:
    def __init__(self, hostname, ip_address, ram_capacity, status):
        self.hostname = hostname
        self.ip_address = ip_address
        self.ram_capacity = ram_capacity
        self.status = status

    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def update_ram(self, new_ram_capacity):
        self.ram_capacity = new_ram_capacity

 
print("\033c")

ragion = input("Enter the region name for the data center: ")
data_center = DataCenter(ragion)

needing = "y"

while needing =="y":
    print("\033c")
    
    hostname = input("Hostname: ")
    ip = input("IP Address: ")
    ram = input("RAM Capacity: ")
    power = input("Status (on/off): ").strip().lower()
    if power == "on":
        power = True
    elif power == "off":
        power = False
    else:
        print("Invalid status. Please enter 'on' or 'off'.")
        continue

    newServer = Server(hostname, ip, ram, power)
    data_center.register_server(newServer)
    
    needing = input("Would you like to add another server? (y/n): ").lower()




print("\n------- Data Center Servers -------")
print(f"Current Region: {data_center.region_name}\n")

for server in data_center.servers:
    print(server.hostname)
    print("-------------------------")
    print(server.ip_address)
    print(server.ram_capacity)
    print(server.status)
            
    if server.status:
        print(f"{server.hostname} is powered on.")
        
    print("\n==========================\n")
    
update = input("Would you like to update one of the servers? (y/n): ").lower()

if update == "y":
    print("1.- Update RAM capacity")
    print("2.- Update Status")
    options = input("Select an option (1 or 2): ")
    match options:
        case "1":
            server_to_update = input("Enter the hostname of the server to update: ")
            
            for server in data_center.servers:
                if server_to_update == server.hostname:
                    new_ram_capacity = input("Enter the new RAM capacity: ")
                    server.update_ram(new_ram_capacity)
                    
                    print(f"{server.hostname} RAM updated to {server.ram_capacity} GB.")
                    break
                            
                else:
                    print("Server not found.")
                    
        case "2":
            for server in data_center.servers:
                if server.status:
                    print("\033c")
                    print(f"{server.hostname} is currently powered on.\n")
                    print("If you want to change its status, please enter the new status (on/off).")
                    print("NOTE: Have in mind that if you turn it off, your other server will turn on automatically.")
                    new_status = input("Enter the new status (on/off): ").lower()
                    
                    if new_status == "on":
                        server.power_on()
                        print(f"{server.hostname} is now powered on.")
                        data_center.servers[1].power_off()
                        print(f"{data_center.servers[1].hostname} is now powered off.")
                    elif new_status == "off":
                        server.power_off()
                        print(f"{server.hostname} is now powered off.")
                        data_center.servers[1].power_on()
                        print(f"{data_center.servers[1].hostname} is now powered on.")
                    else:
                        print("Invalid status. Please enter 'on' or 'off'.")
                    break
                            
                else:
                    print("Server not found.")
                    
    print("\033c")
    print("\n------- Updated Data Center Servers -------\n")
    for server in data_center.servers:
        if server.status:
            print(f"{server.hostname} is powered on.")
            print("-------------------------")
            
else:
    print("\nThank you for using Cloud Infrastructure :)")