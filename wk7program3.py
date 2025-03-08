#Reilly Kurth
#3/7/2025

def us_population():
    data = []

    #user input
    while True:
        #find year, state, and population
        year = input("Enter the year (type done when done): ")
        if year.lower() == "done":
            break
        state = input("Enter the state name: ")
        population = int(input("Enter the population: "))

        #add to list
        data.append([int(year), state, population])


    user_input_year = int(input("Enter the year to calculate total population: "))
    total_population_in_year = 0
    for entry in data:
        if entry[0] == user_input_year:
            total_population_in_year += entry[2]

    # result
    print(f"The total population for {user_input_year} is {total_population_in_year}.")

us_population()