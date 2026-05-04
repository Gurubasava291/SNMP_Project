# Configuration parameters for SNMP GET Request

# Target SNMP Agent
TARGET_IP = "127.0.0.1"  # Default: localhost
PORT = 161               # Default: 161
COMMUNITY_STRING = "public" # Default: public

# OIDs to query
OIDS = {
    "System Name": "1.3.6.1.2.1.1.5.0",
    "System Uptime": "1.3.6.1.2.1.1.3.0"
}
