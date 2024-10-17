# Restaurant 1
restaurant_object_one = {
    "restaurant_id" : 1,
    "restaurant_name" : "Manila Bay Kitchen",
    "restaurant_cuisine" : "Filipino, Bar, Pizza, Seafood, International",
    "restaurant_location" : "Sheraton Manila Bay, Manila"
}
# Restaurant 2
restaurant_object_two = {
    "restaurant_id" : 2,
    "restaurant_name" : "Cafe Ilang-Ilang",
    "restaurant_cuisine" : "Local cuisine, Italian, Chinese, Japanese, American, Filipino",
    "restaurant_location" : "One Rizal Park Manila Hotel"
}
# Restaurant 3
restaurant_object_three = {
    "restaurant_id" : 3,
    "restaurant_name" : "The Aristocrat Restaurant",
    "restaurant_cuisine" : "Filipino",
    "restaurant_location" : "San Andres Street, Manila"
}
# Restaurant 4
restaurant_object_four = {
    "restaurant_id" : 4,
    "restaurant_name" : "Estoria Manila",
    "restaurant_cuisine" : "Filipino, Bar, Cafe, Spanish, Asian",
    "restaurant_location" : "Ermita Ermita Plaza, Manila"
}
# Restaurant 5
restaurant_object_five = {
    "restaurant_id" : 5,
    "restaurant_name" : "Barbara's Heritage Restaurant",
    "restaurant_cuisine" : "Filipino, International, Asian",
    "restaurant_location" : "Intramuros, Manila"
}

# Hold the restaurant dictionaries to restaurants variable
restaurants = [restaurant_object_one,restaurant_object_two,restaurant_object_three,restaurant_object_four,restaurant_object_five]
# Loop through the dictionaries
for restaurant in restaurants:
    # Print the data
    print(f"Restaurant Name: {restaurant.get('restaurant_name')}, Restaurant Cuisine: {restaurant.get('restaurant_cuisine')}, Restaurant Location: {restaurant.get('restaurant_location')}")