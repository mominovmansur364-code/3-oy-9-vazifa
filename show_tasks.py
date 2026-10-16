import csv

def show_tasks():
    with open("tasks.csv", "r", newline="", encoding="utf-8") as fayl:
        oqish = csv.DictReader(fayl)

        for vazifa in oqish:
            print("id:", vazifa["id"])
            print("nomi:", vazifa["name"])
            print("holati:", vazifa["status"])
            print("-" * 20)

show_tasks()
