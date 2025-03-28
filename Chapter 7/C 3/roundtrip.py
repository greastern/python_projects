def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    energy_needed = 2 * distance_one_way/meters_per_energy
    return energy_available >= energy_needed
    