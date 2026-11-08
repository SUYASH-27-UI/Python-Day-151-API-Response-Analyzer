import json
from collections import Counter


def analyze_api_data():

    try:
        with open("users.json", "r") as file:
            data = json.load(file)

        users = data["users"]

        total_users = len(users)
        active_users = 0
        total_age = 0
        departments = Counter()

        for user in users:

            if user["active"]:
                active_users += 1

            total_age += user["age"]

            departments[user["department"]] += 1

        average_age = total_age / total_users if total_users else 0

        print("\n===== API RESPONSE ANALYSIS =====")
        print("Response Status:", data["status"])
        print("Total Users:", total_users)
        print("Active Users:", active_users)
        print("Inactive Users:", total_users - active_users)
        print("Average Age:", round(average_age, 2))

        print("\n===== DEPARTMENT REPORT =====")

        for department, count in departments.items():
            print(department, ":", count)

        report = {
            "total_users": total_users,
            "active_users": active_users,
            "inactive_users": total_users - active_users,
            "average_age": round(average_age, 2),
            "departments": dict(departments)
        }

        with open("analysis_report.json", "w") as file:
            json.dump(report, file, indent=4)

        print("\nReport saved successfully!")

    except FileNotFoundError:
        print("users.json file not found!")

    except (json.JSONDecodeError, KeyError, TypeError) as error:
        print("Invalid JSON data:", error)


analyze_api_data()
