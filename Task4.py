

from Task2 import clean_users, clean_restaurants


restaurant_ratings = {}

for user in clean_users:
    for rid, rating in user["rated"].items():
        rid = int(rid)  # FIX: convert string ID to int
        restaurant_ratings.setdefault(rid, []).append(rating)



avg_ratings = {}
for rid, ratings in restaurant_ratings.items():
    avg_ratings[rid] = sum(ratings) / len(ratings)



sorted_restaurants = sorted(
    avg_ratings.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Top Restaurants:")
for rid, avg in sorted_restaurants:
    print("Restaurant ID:", rid, "Average Rating:", round(avg, 2))



most_active = max(clean_users, key=lambda u: len(u["rated"]))
print("\nMost Active User:", most_active["name"])



category_count = {}

restaurant_map = {r["id"]: r["category"] for r in clean_restaurants}


for user in clean_users:
    for rid in user["rated"]:
        rid = int(rid)  # FIX here also
        category = restaurant_map[rid]
        category_count[category] = category_count.get(category, 0) + 1

popular_category = max(category_count, key=category_count.get)
print("Most Popular Category:", popular_category)
