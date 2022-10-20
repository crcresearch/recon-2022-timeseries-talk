import csv
import random
import datetime
NUMBER_OF_DATA = 1000000


GIS_BOUNDS = {
    'lat_min': 30.38423812849709,
    'lat_max': 48.58350355252427,
    'lon_min': -122.48583545440337,
    'lon_max': -72.78368793608259
}

csv_file = open(f"SAMPLE_DATA_{NUMBER_OF_DATA}.csv", 'w')

csv_obj = csv.DictWriter(csv_file, ["timestamp", "latitude", "longitude"])
csv_obj.writeheader()
print("Generating data...")
for iter in range(0, NUMBER_OF_DATA):
    # generate a new row
    data = {
        "timestamp": datetime.datetime(
            random.randint(1970, 2022),
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(0, 23),
            random.randint(0, 59),
            random.randint(0, 59),
            random.randint(1, 999999)
        ),
        "latitude": random.uniform(GIS_BOUNDS["lat_min"], GIS_BOUNDS["lat_max"]),
        "longitude": random.uniform(GIS_BOUNDS["lon_min"], GIS_BOUNDS["lon_max"])
    }
    csv_obj.writerow(data)
print("done")
