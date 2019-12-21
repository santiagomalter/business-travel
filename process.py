import json
from datetime import datetime, date
from collections import namedtuple
from itertools import takewhile
import reverse_geocode
import argparse

parser = argparse.ArgumentParser(description='Arguments for reporting')
parser.add_argument("--base", default=None, type=str, help="Your base country (eg. Belgium)", required=True)
parser.add_argument("--year", default=None, type=int, help="Year of report (eg. 2019)", required=True)

args = parser.parse_args()

YEAR = args.year
BASE_COUNTRY = args.base

print('📊 Report for %s (base country is "%s")' % (YEAR, BASE_COUNTRY))
print()
print("⏳ Processing...")

Point = namedtuple('Point', 'latitude, longitude, datetime')

def read_points():
    with open('data.json') as f:
        data = json.load(f)

    for point in data['locations']:
        yield Point(
            point['latitudeE7'] / 10 ** 7,
            point['longitudeE7'] / 10 ** 7,
            datetime.fromtimestamp(int(point['timestampMs']) / 1000)
        )

points = read_points()

trips = []

for point in points:
    location = (point.latitude, point.longitude)
    geocode = reverse_geocode.get(location)

    date = point.datetime.date()
    country = geocode["country"]
    duration = (date - trips[-1]["date"]).days if len(trips) > 0 else 0

    if ((len(trips) > 0) and trips[-1]["country"] != country) or len(trips) == 0:
        line = {
            "date": date,
            "country": country,
            "duration": None
        }

        trips.append(line)

        if len(trips) > 1:
            trips[-2]["duration"] = duration # Duration of previous trip

print("✅ Done.")
print()
print("📅 Timeline:")
for trip in trips:
    if trip["date"].year == YEAR and trip["country"] != BASE_COUNTRY and (trip["duration"] != None and trip["duration"] > 0):
        print("  ✈️  %s days in %s, from %s" % (trip["duration"], trip["country"], trip["date"].strftime("%A %d of %B %Y")))
