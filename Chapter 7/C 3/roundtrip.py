def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    energy_needed = 2 * distance_one_way/meters_per_energy
    print(energy_needed)
    print(energy_available)
    if energy_available >= energy_needed:
        return True
    return False
    