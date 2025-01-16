from dotenv import load_dotenv
from prettytable import PrettyTable
import os
import requests

load_dotenv()

payload_inactive = {'inactive': 'false'}
payload_active = {'inactive': 'true'}
active_only = True

if (active_only):
    r = requests.get('https://incidents.fire.ca.gov/umbraco/api/IncidentApi/List', params=payload_inactive)
else:
    r = requests.get('https://incidents.fire.ca.gov/umbraco/api/IncidentApi/List', params=payload_active)

data = r.json()

table = PrettyTable()
table.field_names = ["Fire Name", "Size (in acres)", "Containment %", "Date Started"]
table.align = "c"

for fire in data:
    table.add_row([fire['Name'], fire['AcresBurned'], fire['PercentContained'], fire['StartedDateOnly']])

def main():
    print(table.get_string())

if __name__ == "__main__":
    main()