#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys


total_size = 0
status_code_dict = {}
status_code_list = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        try:
            line_parts = line.split(" ")
            status_code = line_parts[-2]
            file_size = int(line_parts[-1])

            total_size += file_size

            if status_code in status_code_list:
                status_code_dict[status_code] = status_code_dict.get(
                        status_code, 0) + 1

        except (IndexError, ValueError):
            continue

        if line_count % 10 == 0:
            print(f"File size: {total_size}")

            for key, value in sorted(status_code_dict.items()):
                if value != 0:
                    print(f"{key}: {value}")

except KeyboardInterrupt:
    pass

finally:
    print(f"File size: {total_size}")
    for key, value in sorted(status_code_dict.items()):
        if value != 0:
            print(f"{key}: {value}")
