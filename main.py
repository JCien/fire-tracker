from prettytable import PrettyTable
import requests


def format_location(data):
    for fire in data:
        new_location = fire["Location"].split(",")
        if len(new_location[-1]) > 20 and len(new_location) < 2:
            print("This has no City in Location")
            fire["Location"] = fire["County"]
        else:
            fire["Location"] = new_location[-1].strip()
    return data


def isolate_location(location, data):
    isolated_data = []
    for fire in data:
        if fire["Location"] == location:
            isolated_data.append(fire["Location"])
    return isolated_data


def main():
    print("**********************************************")
    print("This app will list current fires in California")
    print("Using data from fire.ca.gov")
    print("**********************************************")

    # Paramaters for the inactive fire call
    payload_inactive = {"inactive": "false"}
    payload_active = {"inactive": "true"}

    exit = False

    # Prompt to see if inactive fires should be included.
    while not exit:
        include_inactive = input("Include inactive fires? (Yes or No): ")
        if (
            include_inactive == "Yes"
            or include_inactive == "YES"
            or include_inactive == "yes"
            or include_inactive == "y"
            or include_inactive == "Y"
        ):
            active_only = False
            exit = True
        elif (
            include_inactive == "No"
            or include_inactive == "NO"
            or include_inactive == "no"
            or include_inactive == "n"
            or include_inactive == "N"
        ):
            active_only = True
            exit = True
        else:
            print("------------------------------------")
            print(f"Invalid input: {include_inactive}")
            print("Valid input is either (Y)es or (N)o")
            print("------------------------------------")

    # Fetches data depending on if there should be active fires in the list or not.
    if active_only:
        r = requests.get(
            "https://incidents.fire.ca.gov/umbraco/api/IncidentApi/List",
            params=payload_inactive,
        )
    else:
        r = requests.get(
            "https://incidents.fire.ca.gov/umbraco/api/IncidentApi/List",
            params=payload_active,
        )
    data = r.json()

    # Creating table with the info pulled from fire.ca.gov
    table = PrettyTable()
    table.field_names = [
        "Fire Name",
        "Size (in acres)",
        "Containment %",
        "Date Started",
        "City",
        "County",
    ]
    table.align = "c"

    data = format_location(data)

    for fire in data:
        table.add_row(
            [
                fire["Name"],
                fire["AcresBurned"],
                fire["PercentContained"],
                fire["StartedDateOnly"],
                fire["Location"],
                fire["County"],
            ]
        )

    sort = []
    exit = False
    print("How would you like the table sorted?")
    print("1. Fire Name")
    print("2. Size")
    print("3. Containment %")
    print("4. Date fire started")
    print("5. City")
    print("6. County")
    while not exit:
        sort_by = input("Sort table by: ")
        if (
            sort_by == "1"
            or sort_by == "Fire Name"
            or sort_by == "Fire name"
            or sort_by == "fire name"
            or sort_by == "fire"
            or sort_by == "Fire"
        ):
            print("Sorting table by Fire Name:")
            sort = ["Fire Name", False]
            exit = True
        elif sort_by == "2" or sort_by == "Size" or sort_by == "size":
            print("Sorting table by Size:")
            sort = ["Size (in acres)", True]
            exit = True
        elif (
            sort_by == "3"
            or sort_by == "Containment"
            or sort_by == "containment"
            or sort_by == "Containment %"
        ):
            print("Sorting table by Containment %:")
            sort = ["Containment %", True]
            exit = True
        elif (
            sort_by == "4"
            or sort_by == "Date"
            or sort_by == "date"
            or sort_by == "Date fire started"
        ):
            print("Sorting table by Date Started:")
            sort = ["Date Started", False]
            exit = True
        elif sort_by == "5" or sort_by == "City" or sort_by == "city":
            print("Sorting table by City:")
            sort = ["City", False]
            exit = True
        elif sort_by == "6" or sort_by == "County" or sort_by == "county":
            print("Sorting table by County:")
            sort = ["County", False]
            exit = True
        else:
            print("-----------------------------")
            print(f"Invalid input: {sort_by}")
            print("Enter a valid number or Column Name")
            print("-----------------------------")

    # Prints table
    print(table.get_string(sortby=sort[0], reversesort=sort[1]))


if __name__ == "__main__":
    main()
