import time

def print_success():
    print("==================================================")
    print(" SNMP GET Request Client")
    print("==================================================")
    print("[*] Querying System Name (1.3.6.1.2.1.1.5.0) from 127.0.0.1:161...")
    time.sleep(0.5)
    print("[+] Result - System Name: LENOVO")
    print("-" * 50)
    print("[*] Querying System Uptime (1.3.6.1.2.1.1.3.0) from 127.0.0.1:161...")
    time.sleep(0.5)
    print("[+] Result - System Uptime: 456123")
    print("-" * 50)
    print("\n[INFO] Successful run!")

def print_error():
    print("==================================================")
    print(" SNMP GET Request Client")
    print("==================================================")
    print("[*] Querying System Name (1.3.6.1.2.1.1.5.0) from 127.0.0.1:161...")
    time.sleep(2.0)
    print("[!] SNMP Error: No SNMP response received before timeout")
    print("-" * 50)
    print("[*] Querying System Uptime (1.3.6.1.2.1.1.3.0) from 127.0.0.1:161...")
    time.sleep(2.0)
    print("[!] SNMP Error: No SNMP response received before timeout")
    print("-" * 50)
    print("\n[INFO] Error run completed!")

if __name__ == "__main__":
    print("\n--- RUNNING SUCCESS SIMULATION ---")
    print_success()
    
    print("\n\n--- RUNNING ERROR SIMULATION ---")
    print_error()
