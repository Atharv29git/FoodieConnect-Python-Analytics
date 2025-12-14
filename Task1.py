

import json




with open("Data.json", "r") as file:
    data = json.load(file)

print("*******************************")
print("USERS WITH RATINGS")
for user in data["users"]:
    print(user["name"], "=", user["rated"])

print("*******************************")


print("\nRESTAURANTS")
for r in data["restaurants"]:
    print(r["id"], "-", r["name"], "(", r["category"], ")")
print("*******************************")

