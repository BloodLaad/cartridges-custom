from cartridges.game import Game

def GetCustomGames(source_id, import_time):
    # Build game
    values = {
        "source": source_id,
        "added": import_time,
        "name": "Yielded Custom Game",
        "game_id": "YieldedCustomGame",
        "executable": "lutris"
    }
    game = Game(values)
    additional_data = {}

    return [(game, additional_data)]