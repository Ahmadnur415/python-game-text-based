from .. import interface


def run(battle):

    while True:

        battle.run_turn()

        if battle.fled:
            return "fled"

        if battle.player.health <= 0:
            return  battle.LOSE

        if battle.enemy.health <= 0:
            return  battle.WIN

def run_turn(battle):
    
    battle.run_player_turn()
    battle.count_turn += 1
    
    if battle.fled or battle.enemy.health <= 0:
        return

    battle.run_enemy_turn()

    print("\n")