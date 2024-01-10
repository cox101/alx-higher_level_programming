#!/usr/bin/python3

import sys

def compute_metrics():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            parts = line.split()

            if len(parts) >= 10:
                status_code = parts[-2]
                file_size = int(parts[-1])

                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

                if i % 10 == 0:
                    print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)

def print_metrics(total_size, status_codes):
    print("Total file size:", total_size)
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    compute_metrics()

