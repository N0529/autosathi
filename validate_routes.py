"""
validate_routes.py
Run this before submitting a PR to check your route file is correct.

Usage: python scripts/validate_routes.py routes/pune/your-route.json
"""

import json
import sys
import os

REQUIRED_ROUTE_FIELDS = ["id", "name", "from_area", "to_area", "city", "is_active"]
REQUIRED_STOP_FIELDS = ["sequence", "name", "landmark", "latitude", "longitude"]
REQUIRED_FARE_FIELDS = ["from_stop", "to_stop", "amount_rupees"]

def validate(filepath):
    errors = []

    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        sys.exit(1)

    with open(filepath) as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            sys.exit(1)

    # Check top-level keys
    for key in ["route", "stops", "fares"]:
        if key not in data:
            errors.append(f"Missing top-level key: '{key}'")

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        sys.exit(1)

    # Validate route fields
    for field in REQUIRED_ROUTE_FIELDS:
        if field not in data["route"]:
            errors.append(f"Route missing field: '{field}'")

    # Validate stops
    stop_sequences = []
    for i, stop in enumerate(data["stops"]):
        for field in REQUIRED_STOP_FIELDS:
            if field not in stop:
                errors.append(f"Stop {i+1} missing field: '{field}'")
        stop_sequences.append(stop.get("sequence"))

        lat = stop.get("latitude", 0)
        lon = stop.get("longitude", 0)
        if not (15 <= lat <= 25 and 68 <= lon <= 90):
            errors.append(f"Stop {i+1} '{stop.get('name')}' coordinates look wrong — expected somewhere in India")

    # Validate fares
    for i, fare in enumerate(data["fares"]):
        for field in REQUIRED_FARE_FIELDS:
            if field not in fare:
                errors.append(f"Fare {i+1} missing field: '{field}'")
        if fare.get("from_stop") not in stop_sequences:
            errors.append(f"Fare {i+1} references unknown from_stop: {fare.get('from_stop')}")
        if fare.get("to_stop") not in stop_sequences:
            errors.append(f"Fare {i+1} references unknown to_stop: {fare.get('to_stop')}")
        if fare.get("amount_rupees", 0) <= 0:
            errors.append(f"Fare {i+1} has invalid amount: {fare.get('amount_rupees')}")

    if errors:
        print(f"\nFound {len(errors)} error(s) in {filepath}:\n")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        stops = len(data["stops"])
        fares = len(data["fares"])
        print(f"\n✓ {filepath} looks good!")
        print(f"  Route : {data['route']['name']}")
        print(f"  Stops : {stops}")
        print(f"  Fares : {fares} pairs")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_routes.py <path-to-route.json>")
        sys.exit(1)
    validate(sys.argv[1])
