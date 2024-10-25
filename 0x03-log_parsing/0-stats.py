#!/usr/bin/python3
"""
this module returns something complicated that i don't want to know
how i did it
"""
import sys
import signal
import re


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# Initialize dictionaries and counters
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0


# Regex pattern for parsing log lines
log_pattern = re.compile(
    r'(\S+) - \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )


def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


# Read from stdin
for line in sys.stdin:
    line_count += 1
    match = log_pattern.match(line)
    if match:
        ip, date, status_code, file_size = match.groups()
        total_size += int(file_size)
        status_code = int(status_code)
        if status_code in status_codes:
            status_codes[status_code] += 1

    if line_count % 10 == 0:
        print_stats()

# Print final stats on exit
print_stats()
