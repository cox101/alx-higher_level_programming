#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""

import sys

def compute_metrics(lines):
    total_size = 0
    status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    for line in lines:
        parts = line.split()
        if len(parts) >= 9:
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_size += file_size
                if status_code in status_code_count:
                    status_code_count[status_code] += 1
            except ValueError:
                pass

    return total_size, status_code_count

def print_statistics(total_size, status_code_count):
    print(f"File size: {total_size}")
    for status_code in sorted(status_code_count.keys()):
        count = status_code_count[status_code]
        if count > 0:
            print(f"{status_code}: {count}")

def main():
    try:
        lines = []
        for line in sys.stdin:
            lines.append(line)
            if len(lines) == 10:
                total_size, status_code_count = compute_metrics(lines)
                print_statistics(total_size, status_code_count)
                lines = []

    except KeyboardInterrupt:
        total_size, status_code_count = compute_metrics(lines)
        print_statistics(total_size, status_code_count)

if __name__ == "__main__":
    main()

