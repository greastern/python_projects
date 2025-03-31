def calculate_flurry_crit(num_attacks, base_damage):
    if num_attacks == 0:
        total_damage = 0
        return total_damage
    for i in range(num_attacks):
        crit_hit = ((base_damage + base_damage) * (num_attacks)) - (base_damage * 2)
   
        total_damage = crit_hit + (base_damage * 4)
        return total_damage 