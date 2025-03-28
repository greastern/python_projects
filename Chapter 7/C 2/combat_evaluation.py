def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage, disadvantage, evenly_matched = True, False, False
    elif player_power < enemy_defense:
        advantage, disadvantage, evenly_matched = False, True, False
    else:
        advantage, disadvantage, evenly_matched = False, False, True

    return advantage, disadvantage, evenly_matched
