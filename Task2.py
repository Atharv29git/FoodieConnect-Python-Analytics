


import json

with open("Data.json", "r") as file:
    data = json.load(file)


clean_users = []
for user in data["users"]:
    if user["name"].strip() != "":
        clean_users.append(user)


for user in clean_users:
    valid_ratings = {}
    for rid, rating in user["rated"].items():
        if 1 <= rating <= 5:
            valid_ratings[rid] = rating
    user["rated"] = valid_ratings


unique_restaurants = {}
for r in data["restaurants"]:
    unique_restaurants[r["id"]] = r

clean_restaurants = list(unique_restaurants.values())


print("*******************************")
print("Cleaned Users:", clean_users)
print("*******************************")
print("Cleaned Restaurants:", clean_restaurants)
print("*******************************")