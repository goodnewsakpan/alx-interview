#!/usr/bin/python3
import sys
import signal

# Initialize global variables
total_file_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """Prints the statistics of file size and status codes."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def handle_signal(sig, frame):
    """Handles the interrupt signal and prints the stats before exiting."""
    print_stats()
    sys.exit(0)

# Register the signal handler for interrupt (CTRL + C)
signal.signal(signal.SIGINT, handle_signal)

try:
    for line in sys.stdin:
        # Split the line into components based on space
        parts = line.split()

        # Skip lines that do not have the expected number of parts
        if len(parts) < 7:
            continue

        # Extract the relevant parts of the line
        ip_address = parts[0]
        date = parts[3][1:]  # Remove the leading '[' from the date
        request = parts[5][1:]  # Remove the leading '"' from the request
        status_code = parts[-2]
        file_size = parts[-1]

        # Ensure the line matches the expected format
        if request != "GET":
            continue

        # Convert file size to an integer
        try:
            file_size = int(file_size)
            total_file_size += file_size
        except ValueError:
            continue

        # Count the status code if it's one of the expected ones
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)

# Print final stats if the loop ends
print_stats()
