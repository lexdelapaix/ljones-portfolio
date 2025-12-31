#!/usr/bin/env python3
"""
Taxi Meter / Mileage Fare Calculator

- Base fare (flag drop)
- Per-mile charge
- Optional per-minute charge (driving time)
- Optional waiting fee (per minute)
- Supports single trip OR multiple trips tally

Run:
  python taxi_meter.py
"""

from dataclasses import dataclass

@dataclass
class RateCard:
    base_fare: float = 3.50          # flag drop
    per_mile: float = 2.25           # $ per mile
    per_minute: float = 0.35         # $ per driving minute (optional)
    waiting_per_minute: float = 0.50 # $ per waiting minute (optional)


def money(x: float) -> str:
    return f"${x:,.2f}"


def calc_fare(miles: float, driving_minutes: float, waiting_minutes: float, rates: RateCard) -> float:
    if miles < 0 or driving_minutes < 0 or waiting_minutes < 0:
        raise ValueError("Miles/minutes can't be negative.")
    return (
        rates.base_fare
        + miles * rates.per_mile
        + driving_minutes * rates.per_minute
        + waiting_minutes * rates.waiting_per_minute
    )


def ask_float(prompt: str, default: float = 0.0) -> float:
    raw = input(prompt).strip()
    if raw == "":
        return default
    return float(raw)


def main():
    print("\n🚕 Taxi Meter Tally\n")
    print("Enter trip info. Press Enter to use 0 for minutes. Type 'done' when finished.\n")

    # Set your rate card here (edit these values)
    rates = RateCard(
        base_fare=3.50,
        per_mile=2.25,
        per_minute=0.00,          # set to 0.35 if you want time-based driving charges
        waiting_per_minute=0.00,  # set to 0.50 if you want waiting charges
    )

    total = 0.0
    trip_count = 0

    print(f"Rate card: base {money(rates.base_fare)} | per mile {money(rates.per_mile)}"
          f" | per minute {money(rates.per_minute)} | waiting/min {money(rates.waiting_per_minute)}\n")

    while True:
        raw = input("Miles for this trip (or 'done'): ").strip().lower()
        if raw in ("done", "d", "q", "quit", "exit"):
            break
        if raw == "":
            print("Enter miles (example: 12.4) or 'done'.\n")
            continue

        try:
            miles = float(raw)
            driving_minutes = ask_float("Driving minutes (optional, Enter=0): ", 0.0)
            waiting_minutes = ask_float("Waiting minutes (optional, Enter=0): ", 0.0)

            fare = calc_fare(miles, driving_minutes, waiting_minutes, rates)
            trip_count += 1
            total += fare

            print(f"Trip #{trip_count}: {miles} mi -> {money(fare)} | Running total: {money(total)}\n")

        except ValueError as e:
            print(f"❌ Input error: {e}\n")

    print("\n✅ Summary")
    print(f"Trips: {trip_count}")
    print(f"Total: {money(total)}\n")


if __name__ == "__main__":
    main()