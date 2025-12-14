

from Task2 import clean_users



def recommend_restaurants(target_user, users):
    recommendations = set()



    target_rated = {int(rid): rating for rid, rating in target_user["rated"].items()}

    for user in users:
        if user["id"] == target_user["id"]:
            continue




        user_rated = {int(rid): rating for rid, rating in user["rated"].items()}

    

        shared = set(target_rated.keys()) & set(user_rated.keys())

        if shared:
            for rid, rating in user_rated.items():
                if rid not in target_rated and rating >= 4:
                    recommendations.add(rid)

    return recommendations



user = clean_users[0]
result = recommend_restaurants(user, clean_users)

print("Recommended restaurants for", user["name"], ":", result)
