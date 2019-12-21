# (1) Setup
1. Checkout the repository
2. Create an env and activate it

```
$ python3 -m venv env
$ source env/bin/activate
```

4. Install requirements
```
$ pip install -r requirements.txt
```

# (2) Export data from Google

1. Go to Google Takeout here: https://takeout.google.com/settings/takeout
2. Unselect everything except "Location History" and click "Next step"
3. Choose "Create Archive"
4. Wait a few minutes or hours depending on the file size and check your mail box
5. Click on the link received to download a ZIP containing the full history
6. Copy the main JSON file to the root folder and rename it to "data.json"

# (3) Run

Example:

```
$ python process.py --base Belgium --year 2019

📊 Report for 2019 (base country is "Belgium")

⏳ Processing...
✅ Done.

📅 Timeline:
  ✈️  1 days in United Kingdom, from Tuesday 19 of February 2019
  ✈️  10 days in Argentina, from Wednesday 20 of February 2019
  ✈️  1 days in Chile, from Saturday 02 of March 2019
  ✈️  22 days in Mexico, from Sunday 03 of March 2019
  ✈️  1 days in Spain, from Monday 25 of March 2019
  ✈️  4 days in France, from Thursday 28 of March 2019
  ✈️  23 days in Spain, from Wednesday 15 of May 2019
  ✈️  1 days in France, from Tuesday 11 of June 2019
  ✈️  17 days in Spain, from Wednesday 12 of June 2019
  ✈️  1 days in Spain, from Sunday 30 of June 2019
  ✈️  15 days in Spain, from Friday 05 of July 2019
  ✈️  20 days in Spain, from Thursday 25 of July 2019
  ✈️  7 days in Spain, from Sunday 18 of August 2019
  ✈️  9 days in France, from Sunday 25 of August 2019
  ✈️  7 days in Spain, from Tuesday 03 of September 2019
  ✈️  16 days in Spain, from Sunday 15 of September 2019
  ✈️  17 days in Spain, from Wednesday 09 of October 2019
  ✈️  4 days in Spain, from Saturday 26 of October 2019
  ✈️  1 days in France, from Wednesday 30 of October 2019
  ✈️  1 days in Switzerland, from Thursday 31 of October 2019
  ✈️  6 days in Spain, from Friday 01 of November 2019
  ✈️  15 days in Spain, from Friday 29 of November 2019
```
