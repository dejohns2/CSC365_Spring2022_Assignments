#!/usr/bin/env python3

# Author: Debbie Johnson
# Written: 2021.03.15

# tuple that can't be changed once it's created
# closest distance from the sun in millions of a mile
# https://www.universetoday.com/15462/how-far-are-the-planets-from-the-sun/
planets = (
    ('Earth', 91),
    ('Jupiter', 460),
    ('Mars', 127),
    ('Mercury', 29),
    ('Neptune', 2770),
    ('Saturn', 839),
    ('Uranus', 1710),
    ('Venus', 66)
)


# get the selected planet's distance from the sun
def get_planet_distance(selected_planet):
    # iterate through the planets tuple
    for planet_info in planets:

        planet, distance = planet_info  # unpack tuple

        if planet == selected_planet:
            return distance  # return the planet's distance from the sun

    return -1  # if planet is not in the tuple then return -1 as an error indicator


# generated a list for each planet's distance from the selected planet
def distance_from_planet(selected_planet):
    distance_list = []  # create an empty list

    selected_distance = get_planet_distance(selected_planet)  # get the selected planet's distance from the sun

    if selected_distance == -1:
        print('Error! Unable to locate', selected_planet, 'in list.')
        return

    # iterate through the planets tuple
    for planet_info in planets:

        planet, distance = planet_info  # unpack list

        # only compare planets that is not the selected planet
        if planet != selected_planet:

            planet_difference = abs(distance - selected_distance)  # get the absolute value (removes the negative sign)
            distance_list.append([planet, planet_difference])

    # https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
    # https://www.w3schools.com/python/python_lambda.asp
    distance_list.sort(key=lambda x: x[1])

    # display the distance report
    display_distances(selected_planet, distance_list)


# display the generated list for each planet's distance from the selected planet
def display_distances(selected_planet, distance_list):
    # iterate through the distance_list that was just created
    for planet_info in distance_list:

        planet, distance = planet_info

        print(planet, 'is', distance, 'million miles from', selected_planet)


# display the all the planet's names from the tuple list
def display_planets():
    print("planets: ", end='')  # elimiate the newline

    # iterate through the planets tutple
    for planet_info in planets:

        planet, distance = planet_info  # unpack tuple

        print(planet, end=' ')  # display each planet name followed by a space instead of newline

    print()


# main function that keeps the program looping until the user enter q for quit
def main():
    while True:
        print('=' * 70)
        display_planets()  # display a list of valid planet namers
        selected_planet = input('Please enter one of the above planet names or q to quit: ')
        print('=' * 70)
        print()

        # handle for both capital and lower case letter q
        if selected_planet.lower() == 'q' or 'quit':
            print('Live Long and Prosper V')
            return

        # capitalize the planet name in case the user didn't enter it that way
        distance_from_planet(selected_planet.capitalize())
        print()


# if this is the starting module then run the main function
if __name__ == "__main__":
    main()
