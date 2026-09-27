import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT_DIR = Path("visualizations")
OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Flights by airline
df = pd.read_csv("flights_by_airline.csv")

plt.figure(figsize=(10, 6))
plt.bar(df["airline"], df["total_flights"])
plt.title("Total Flights by Airline")
plt.xlabel("Airline")
plt.ylabel("Number of Flights")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "flights_by_airline.png", dpi=300)
plt.close()


# 2. Average departure vs arrival delay
departure = pd.read_csv("departure_delay_by_airline.csv")
arrival = pd.read_csv("arrival_delay_by_airline.csv")

delay = pd.merge(departure, arrival, on="airline")

x = range(len(delay))
width = 0.35

plt.figure(figsize=(11, 6))
plt.bar(
    [i - width / 2 for i in x],
    delay["avg_departure_delay"],
    width,
    label="Departure Delay"
)
plt.bar(
    [i + width / 2 for i in x],
    delay["avg_arrival_delay"],
    width,
    label="Arrival Delay"
)

plt.title("Average Departure and Arrival Delay by Airline")
plt.xlabel("Airline")
plt.ylabel("Average Delay (minutes)")
plt.xticks(x, delay["airline"], rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "average_delays_by_airline.png", dpi=300)
plt.close()


# 3. Monthly average departure delay
monthly = pd.read_csv("monthly_delay.csv")

plt.figure(figsize=(10, 6))
plt.bar(monthly["month"], monthly["avg_departure_delay"])
plt.title("Monthly Average Departure Delay")
plt.xlabel("Month")
plt.ylabel("Average Departure Delay (minutes)")
plt.xticks(range(1, 13))
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_average_delay.png", dpi=300)
plt.close()


# 4. Cancellations by airline
cancel = pd.read_csv("cancellations_by_airline.csv")

plt.figure(figsize=(10, 6))
plt.bar(cancel["airline"], cancel["cancelled_flights"])
plt.title("Cancelled Flights by Airline")
plt.xlabel("Airline")
plt.ylabel("Number of Cancelled Flights")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "cancellations_by_airline.png", dpi=300)
plt.close()


# 5. Top 10 airports by delayed flights
airport = pd.read_csv("airport_delays.csv")

plt.figure(figsize=(10, 6))
plt.barh(
    airport["origin_airport"][::-1],
    airport["delayed_flights"][::-1]
)
plt.title("Top 10 Origin Airports by Delayed Flights")
plt.xlabel("Number of Delayed Flights")
plt.ylabel("Origin Airport")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "airport_delays.png", dpi=300)
plt.close()


# 6. Delay causes
causes = pd.read_csv("delay_causes.csv")

cause_names = [
    "Airline Delay",
    "Weather Delay",
    "Air System Delay",
    "Late Aircraft Delay",
    "Security Delay"
]

cause_values = [
    causes["airline_delay"].iloc[0],
    causes["weather_delay"].iloc[0],
    causes["air_system_delay"].iloc[0],
    causes["late_aircraft_delay"].iloc[0],
    causes["security_delay"].iloc[0]
]

plt.figure(figsize=(10, 6))
plt.bar(cause_names, cause_values)
plt.title("Total Delay by Cause")
plt.xlabel("Delay Cause")
plt.ylabel("Total Delay (minutes)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "delay_causes.png", dpi=300)
plt.close()


print("All visualizations created successfully!")
print(f"Charts saved in: {OUTPUT_DIR}")
