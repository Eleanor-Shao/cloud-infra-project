#!/usr/bin/env python3
import sys

max_temperatures = {}

for line in sys.stdin:
    line = line.strip()
    # Split the line into yearMonthDay and temperature
    yearMonthDay, temperature = line.split('\t', 1)
    temperature = int(temperature)

    # If this yearMonthDay isn't in our dictionary yet or if this temperature is higher than the current max, update it
    if yearMonthDay not in max_temperatures or temperature > max_temperatures[yearMonthDay]:
        max_temperatures[yearMonthDay] = temperature

# Print out our final result
for yearMonthDay in max_temperatures:
    print(f"{yearMonthDay}\t{max_temperatures[yearMonthDay]}")
