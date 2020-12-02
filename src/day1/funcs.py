import math


def calc_fuel_for_mass(mass):
    fuel = mass / 3
    fuel = math.floor(fuel)
    fuel -= 2
    return fuel


def calc_fuel_for_fuel(fuel_mass):
    total_fuel_for_mod_fuel = 0
    mass_remaining = fuel_mass
    while mass_remaining > 0:
        fuel_needed = calc_fuel_for_mass(mass_remaining)
        mass_remaining = fuel_needed
        if mass_remaining > 0:
            total_fuel_for_mod_fuel += fuel_needed
    return total_fuel_for_mod_fuel
