import subprocess
import ipaddress

def scanner():
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:
        fullNetstat = subprocess.check_output(
            ['netstat', '-n'],
            stderr=subprocess.DEVNULL,
            startupinfo=startupinfo
        ).decode(errors='ignore')
    except subprocess.CalledProcessError:
        print("Error running netstat.")
        return []
    
    lines = fullNetstat.splitlines()
    activeConnections = []


    while lines and not lines[0].strip().startswith("Proto"):
        lines.pop(0)

    for line in lines:
        parts = line.split()
        if len(parts) < 3:
            continue
        address = parts[2]


        ip = address.rsplit(':', 1)[0].replace('[', '').replace(']', '')
        try:
            ipaddress.ip_address(ip)
            activeConnections.append(ip)
        except ValueError:
            continue

    return activeConnections
