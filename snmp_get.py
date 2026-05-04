"""
snmp_get.py
A beginner-friendly Python script to perform an SNMP GET request.
It retrieves System Name and System Uptime from a local SNMP agent.
"""

from pysnmp.hlapi import *
import config

def perform_snmp_get(target_ip, port, community, oid_name, oid_value):
    """
    Performs an SNMP GET request for a specific OID.
    
    Args:
        target_ip (str): IP address of the target SNMP agent.
        port (int): Port of the target SNMP agent.
        community (str): SNMP community string.
        oid_name (str): Human-readable name of the OID.
        oid_value (str): The OID string.
    """
    try:
        print(f"[*] Querying {oid_name} ({oid_value}) from {target_ip}:{port}...")
        
        # Construct the SNMP GET request using pysnmp High-Level API
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community, mpModel=0), # SNMPv1 (use mpModel=1 for SNMPv2c)
            UdpTransportTarget((target_ip, port), timeout=2.0, retries=1),
            ContextData(),
            ObjectType(ObjectIdentity(oid_value))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        # Handle potential errors
        if errorIndication:
            # Connection or timeout errors
            print(f"[!] SNMP Error: {errorIndication}")
        elif errorStatus:
            # Errors from the SNMP agent (e.g., Invalid OID)
            print(f"[!] Agent Error: {errorStatus.prettyPrint()} at "
                  f"{errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}")
        else:
            # Success: print the result
            for varBind in varBinds:
                # varBind is a tuple: (OID, Value)
                print(f"[+] Result - {oid_name}: {varBind[1].prettyPrint()}")

    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")

def main():
    print("="*50)
    print(" SNMP GET Request Client")
    print("="*50)
    
    # Iterate through the configured OIDs and perform requests
    for name, oid in config.OIDS.items():
        perform_snmp_get(
            target_ip=config.TARGET_IP,
            port=config.PORT,
            community=config.COMMUNITY_STRING,
            oid_name=name,
            oid_value=oid
        )
        print("-" * 50)

if __name__ == "__main__":
    main()
