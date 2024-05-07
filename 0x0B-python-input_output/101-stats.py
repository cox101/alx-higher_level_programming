#!/usr/bin/python3

import sys

def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def process_input_line(line, total_size, status_codes):
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = parts[-2]

        total_size += size

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

        return total_size, status_codes

    except (ValueError, IndexError):
        return total_size, status_codes

def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            total_size, status_codes = process_input_line(line, total_size, status_codes)

            if i % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()
