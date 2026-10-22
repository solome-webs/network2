import random

print("-" * 50)
print("Welcome to the network-router configuration menu")
print("-" * 50)

subnet_range = {
    'A': '255.0.0.0',
    'B': '255.255.0.0',
    'C': '255.255.255.0',
    'D': '255.255.255.240',
    'E': '255.255.255.240'
}

try:
    account_name = input("Enter your name: ")
    print(f"Hello {account_name}, welcome to the network-router configuration menu!")
    print("Do you want to configure your router?")
    print("-" * 50)
    print("Options:")
    print("1. yes")
    print("2. no")
    print("-" * 50)
    
    user_choice = input("Enter your choice (yes/no): ").strip().lower()
    
    if user_choice == "yes":
        print("Please select the configuration method:")
        while True:
            print("1. Manual Configuration")
            print("2. Dynamic Configuration")
            
            try:
                router_choice = int(input("Enter your choice (1-2): "))
            except ValueError:
                print("Error: Please enter a valid number (1-2).")      
                continue  
                
            if router_choice == 1:
                print("You have selected Manual Configuration.")
                ip_class = ''
                while True:
                    ip_address = input("Enter the IP address: ").strip()
                    
                    if ip_address.count('.') == 3 and all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_address.split('.')):
                        first_octet = int(ip_address.split('.')[0])
                        
                        if 1 <= first_octet <= 126:
                            ip_class = 'A' 
                            print("Class A IP address detected.")
                            print(f'Subnet mask for class A is {subnet_range["A"]}')
                        elif 128 <= first_octet <= 191:
                            ip_class = 'B'  
                            print("Class B IP address detected.")
                            print(f'Subnet mask for class B is {subnet_range["B"]}')
                        elif 192 <= first_octet <= 223:
                            ip_class = 'C'  
                            print("Class C IP address detected.")
                            print(f'Subnet mask for class C is {subnet_range["C"]}')
                        elif 224 <= first_octet <= 239:
                            ip_class = 'D'
                            print("Class D IP address detected.")
                            print(f'Subnet mask for class D is {subnet_range["D"]}')
                        elif 240 <= first_octet <= 255:
                            ip_class = 'E'  
                            print("Class E IP address detected.")
                            print(f'Subnet mask for class E is {subnet_range["E"]}')
                        else:
                            print("Error: IP address first octet out of standard range.")
                            continue
                        break  
                    print("Error: Invalid IP address format. Please enter a valid IP address.")

                while True:
                    gateway = input("Enter the Gateway: ").strip()
                    if gateway == ip_address:
                        print("Error: Gateway cannot be the same as the IP address. Please enter a different gateway.")
                        continue
                    break

                print(f"\nRouter configured successfully with IP: {ip_address}")
                print(f"Subnet Mask: {subnet_range[ip_class]}")
                print(f"Gateway: {gateway}")
                
                save_choice = input("Do you want to save this configuration? (yes/no): ").strip().lower()
                if save_choice == "yes":
                    print("Configuration saved successfully!")
                else:
                    print("Configuration not saved.")
                break 
                
            elif router_choice == 2:
                print("You have selected Dynamic Configuration.")
                print("Requesting IP address, Subnet Mask, and Gateway from DHCP server...")
                random_network = random.randint(0, 5)
                random_host = random.randint(2, 254)
                dynamic_ip = f"192.168.{random_network}.{random_host}"
                dynamic_subnet = "255.255.255.0"
                dynamic_gateway = f"192.168.{random_network}.1"
                
                print(f"ip-address: {dynamic_ip}")
                print(f"subnetmask: {dynamic_subnet}")
                print(f"default-gateway: {dynamic_gateway}")
                print("Dynamic configuration applied successfully!")
                print("Thank you for using the network-router configuration menu!")
                break 
            else:
                print("Invalid choice. Please select a valid option (1-2).")
                
    elif user_choice == "no":
        print("Welcome to the other options menu!")
        print("-" * 50)
        while True:
            print("Please select one of the following options:")
            print("1. Reset Router")
            print("2. Update Firmware")
            print("3. Exit")
            print("-" * 50)
            
            try:
                other_choice = int(input("Enter your choice (1-3): "))
                if other_choice == 1:
                    print("Router has been reset to factory settings.")
                elif other_choice == 2:
                    print("Firmware update initiated. Please wait...")
                    print("Firmware updated successfully!")
                elif other_choice == 3:
                    print("Exiting the configuration menu. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a valid option (1-3).")
            except ValueError:
                print("Error: Please enter a valid number (1-3).")        
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")

except ValueError:
    print("Error: Invalid input encountered.")