from dotenv import load_dotenv
from prettytable import PrettyTable
import os

load_dotenv()

api_key = os.getenv("FIRMS_MAP_KEY")

table = PrettyTable()
table.field_names = ["Fire Name", "Size", "Containment %", "Proximity"]
table.align = "c"

def main():
    print(table.get_string())

if __name__ == "__main__":
    main()