# University 1
university_object_one = {
    "university_id" : 1,
    "university_name" : "University of the Philippines",
    "university_location" : "Diliman, Quezon City",
    "university_size" : "493 hectares",
    "university_founded_date" : "February 12, 1949",
    "university_campus" : "Suburban",
}
# University 2
university_object_two = {
    "university_id" : 2,
    "university_name" : "Ateneo de Manila University",
    "university_location" : "Katipunan Ave, Quezon City",
    "university_size" : "83 hectares",
    "university_founded_date" : "December 10, 1859",
    "university_campus" : "Urban"
}
# University 3
university_object_three = {
    "university_id" : 3,
    "university_name" : "University of Santo Tomas",
    "university_location" : "España Blvd, Sampaloc, Manila",
    "university_size" : "21.5 hectares",
    "university_founded_date" : "April 28, 1611",
    "university_campus" : "Urban"
}
# University 4
university_object_four = {
    "university_id" : 4,
    "university_name" : "De La Salle University",
    "university_location" : "Taft Ave, Malate, Manila",
    "university_size" : "5.4 hectares",
    "university_founded_date" : "June 16, 1911",
    "university_campus" : "Urban"
}
# University 5
university_object_five = {
    "university_id" : 5,
    "university_name" : "Mapúa University",
    "university_location" : "Muralla St, Intramuros, Manila",
    "university_size" : "1.79 hectares",
    "university_founded_date" : "January 25, 1925",
    "university_campus" : "Urban"
}

# Hold the university dictionaries to universities variables
universities = [university_object_one,university_object_two,university_object_three,university_object_four,university_object_five]
# Loop through the dictionaries
for university in universities:
    # Print the data
    print(f"University Name: {university.get('university_name')}, University Location: {university.get('university_location')}, University Size: {university.get('university_size')}, University Founded Date: {university.get('university_founded_date')}, University Campus: {university.get('university_campus')}")