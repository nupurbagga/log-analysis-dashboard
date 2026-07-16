import re

ssh_pattern = re.compile(
    r'(?P<month>\w{3})\s+'
    r'(?P<day>\d+)\s+'
    r'(?P<time>\d+:\d+:\d+).*?'
    r'sshd.*?'
    r'(?P<status>Failed|Accepted)\s+password\s+for\s+'
    r'(invalid user\s+)?'
    r'(?P<user>\S+)\s+from\s+'
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
)




def parse_log(text):
    events = []

    for ln,  line in enumerate(text.splitlines(),start = 1):
        match = ssh_pattern.search(line)

        if not match:
            continue

        events.append({
            "line":ln,
            "timestamp": f"{match.group('month')} {match.group('day')} {match.group('time')}",
            "status": match.group("status"),
            "username": match.group("user"),
            "ip": match.group("ip"),
            "raw": line
    })
        
    return events