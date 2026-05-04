# SNMP GetRequest Implementation

This is a beginner-friendly Python project that implements an SNMP GET request to retrieve system information (System Name and System Uptime) from a local SNMP agent.

## Project Description
This tool uses the `pysnmp` library to perform an SNMP GET request against a specified target IP, port, and community string. It queries specific Object Identifiers (OIDs) to retrieve basic system statistics. It handles common errors like timeouts and connection failures gracefully.

## Project Structure
- `config.py`: Contains configurable parameters (IP, Port, Community String, OIDs).
- `snmp_get.py`: Main executable script containing the GET request logic.
- `requirements.txt`: Python dependencies.
- `report.md`: Detailed project report.
- `screenshots/`: Folder for output screenshots. Place your terminal output screenshots in this directory to include them in your final submission.

## Installation Steps

### 1. Install Python Dependencies
Make sure you have Python installed. Then, install the required library (`pysnmp`) using pip:
```bash
pip install -r requirements.txt
```

### 2. Install and Start SNMP Agent (snmpd)
To test this script, you need a running SNMP agent.

**On Windows:**
1. Open "Turn Windows features on or off".
2. Check "Simple Network Management Protocol (SNMP)" and click OK.
3. Open `services.msc`, find the "SNMP Service".
4. Go to Properties -> Security tab. Add an Accepted community name `public` with `READ ONLY` rights.
5. Apply and start/restart the service.

**On Ubuntu/Debian Linux:**
1. Install snmpd:
   ```bash
   sudo apt update
   sudo apt install snmpd
   ```
2. Edit configuration:
   ```bash
   sudo nano /etc/snmp/snmpd.conf
   ```
   Add or ensure this line exists: `rocommunity public default`
3. Restart the service:
   ```bash
   sudo systemctl restart snmpd
   ```

## How to Run the Program
1. Ensure your SNMP agent is running.
2. Edit `config.py` if you need to change the target IP, port, or community string (default is `127.0.0.1`, port `161`, community `public`).
3. Run the script:
```bash
python snmp_get.py
```

## Sample Output
```
==================================================
 SNMP GET Request Client
==================================================
[*] Querying System Name (1.3.6.1.2.1.1.5.0) from 127.0.0.1:161...
[+] Result - System Name: My-Desktop-PC
--------------------------------------------------
[*] Querying System Uptime (1.3.6.1.2.1.1.3.0) from 127.0.0.1:161...
[+] Result - System Uptime: 456123
--------------------------------------------------
```
