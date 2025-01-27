#!/usr/bin/env python3

from prettytable import PrettyTable
import requests
import os
import sys


def clear_screen():
    # For Widows
    if os.name == "nt":
        os.system("cls")
    # For Mac and Linux
    else:
        os.system("clear")


def swap_sort(sort):
    if sort:
        new_sort = False
    else:
        new_sort = True
    return new_sort


def format_location(data):
    for fire in data:
        new_location = fire["Location"].split(",")
        if len(new_location[-1]) > 20 and len(new_location) < 2:
            fire["Location"] = fire["County"]
        else:
            fire["Location"] = new_location[-1].strip()
    return data


def format_percentage(data):
    for fire in data:
        if fire["PercentContained"] == None:
            fire["PercentContained"] = 0.0
    return data


def print_options():
    print("How would you like the table sorted?")
    print("1. Fire Name")
    print("2. Size")
    print("3. Containment %")
    print("4. Date fire started")
    print("5. City")
    print("6. County")


def main():
    clear_screen()
    print("**********************************************")
    print("This app will list current fires in California")
    print("Using data from fire.ca.gov")
    print("**********************************************\n")

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
    clear_screen()

    # Fetches data depending on if there should be active fires in the list or not.
    if active_only:
        try:
            r = requests.get(
                "https://incidents.fire.ca.gov/umbraco/api/IncidentApi/List",
                params=payload_inactive,
            )
        except requests.exceptions.RequestException:
            raise SystemExit(
                "Error: There was a problem communicating with incidents.fire.ca.gov\nPlease check your connection and try again."
            )

    else:
        try:
            r = requests.get(
                "https://incidents.fire.ca.gov/umbraco/api/IncidentApi/List",
                params=payload_active,
            )
        except requests.exceptions.RequestException:
            raise SystemExit(
                "Error: There was a problem communicating with incidents.fire.ca.gov\nPlease check your connection and try again."
            )
    data = r.json()

    # If no data is provided, exit app.
    if len(data) == 0:
        sys.exit("No Data provided from fire.ca.gov...\nTry again later.")

    # Creating table with the info pulled from fire.ca.gov
    table = PrettyTable()
    table.field_names = [
        "1. Fire Name",
        "2. Size (in acres)",
        "3. Containment %",
        "4. Date Started",
        "5. City",
        "6. County",
    ]
    table.align = "c"

    data = format_location(data)
    data = format_percentage(data)

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
    print_options()
    initial = True
    flip_sort = False
    while not exit:
        print("X to exit")
        invalid = False
        sort_by = input("Sort table by: ")
        clear_screen()
        if (
            sort_by == "1"
            or sort_by == "Fire Name"
            or sort_by == "Fire name"
            or sort_by == "fire name"
            or sort_by == "fire"
            or sort_by == "name"
            or sort_by == "Fire"
        ):
            print("Sorting table by Fire Name:")
            flip_sort = swap_sort(flip_sort)
            sort = ["1. Fire Name", flip_sort]
        elif sort_by == "2" or sort_by == "Size" or sort_by == "size":
            print("Sorting table by Size:")
            flip_sort = swap_sort(flip_sort)
            sort = ["2. Size (in acres)", flip_sort]
        elif (
            sort_by == "3"
            or sort_by == "Containment"
            or sort_by == "containment"
            or sort_by == "Containment %"
            or sort_by == "%"
        ):
            print("Sorting table by Containment %:")
            flip_sort = swap_sort(flip_sort)
            sort = ["3. Containment %", flip_sort]
        elif (
            sort_by == "4"
            or sort_by == "Date"
            or sort_by == "date"
            or sort_by == "Date fire started"
        ):
            print("Sorting table by Date Started:")
            flip_sort = swap_sort(flip_sort)
            sort = ["4. Date Started", flip_sort]
        elif sort_by == "5" or sort_by == "City" or sort_by == "city":
            print("Sorting table by City:")
            flip_sort = swap_sort(flip_sort)
            sort = ["5. City", flip_sort]
        elif sort_by == "6" or sort_by == "County" or sort_by == "county":
            print("Sorting table by County:")
            flip_sort = swap_sort(flip_sort)
            sort = ["6. County", flip_sort]
        elif (
            sort_by == "X"
            or sort_by == "x"
            or sort_by == "exit"
            or sort_by == "Exit"
            or sort_by == "EXIT"
        ):
            exit = True
        else:
            print("-----------------------------")
            print(f"Invalid input: {sort_by}")
            print("Enter a valid number or Column Name")
            print("-----------------------------")
            invalid = True
            if initial:
                print_options()

        # Prints table
        if exit:
            sys.exit()
        elif invalid and initial:
            continue
        else:
            initial = False
            print(table.get_string(sortby=sort[0], reversesort=sort[1]))
    clear_screen()


if __name__ == "__main__":
    main()
