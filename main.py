from dotenv import load_dotenv
from prettytable import PrettyTable
import sys
import requests

load_dotenv()

print("*****")
print("This app will list current fires in California")
print("Using data from fire.ca.gov")
print("*****")

include_inactive = input("Include inactive fires? (Yes or No): ")

payload_inactive = {'inactive': 'false'}
payload_active = {'inactive': 'true'}

if (include_inactive == "Yes" or include_inactive == "yes" or include_inactive == "y" or include_inactive == "Y"):
    active_only = False
elif (include_inactive == "No" or include_inactive == "no" or include_inactive == "n" or include_inactive == "N"):
    active_only = True
else:
    print(f"Invalid input: {include_inactive}")
    print("Valid input is either (Y)es or (N)o")
    sys.exit(1)

if (active_only):
    r = requests.get('https://incidents.fire.ca.gov/umbraco/api/IncidentApi/List', params=payload_inactive)
else:
    r = requests.get('https://incidents.fire.ca.gov/umbraco/api/IncidentApi/List', params=payload_active)

data = r.json()

table = PrettyTable()
table.field_names = ["Fire Name", "Size (in acres)", "Containment %", "Date Started", "County"]
table.align = "c"
table.align["Fire Name"] = "l"
for fire in data:
    table.add_row([fire['Name'], fire['AcresBurned'], fire['PercentContained'], fire['StartedDateOnly'], fire['County']])

def main():
    print(table.get_string(sortby="Size (in acres)", reversesort=True))

if __name__ == "__main__":
    main()