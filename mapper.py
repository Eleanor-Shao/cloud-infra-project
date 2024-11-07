#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Strip out the line endings and leading/trailing whitespace
    line = line.strip()
    # Extract yearMonthDay (characters 15-23) and temperature (characters 88-92)
    # as well as the quality (characters 92-93)
    yearMonthDay = line[15:23]
    temperature = line[87:92]
    quality = line[92:93]

    # Skip the line if the temperature is +9999 (missing data) or quality is not in the accepted range
    if temperature != "+9999" and quality in ['0', '1', '4', '5', '9']:
        print(f"{yearMonthDay}\t{temperature}")
