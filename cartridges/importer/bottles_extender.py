import os
import json
from pathlib import Path
from datetime import datetime, timezone
from cartridges.game import Game
from cartridges.importer.extender_data import root_dir

def GetCustomGames(source_id, import_time):
    games = []
    subfolders = [f for f in os.scandir(root_dir) if f.is_dir()]
    if len(subfolders) == 0:
        return games
    for game_dir in subfolders:
        meta_path = os.path.join(game_dir.path, ".meta")
        if os.path.exists(meta_path):
            data_path = os.path.join(game_dir.path, ".meta/data.json")
            if os.path.exists(data_path):
                data = {}
                with open(data_path, 'r') as json_file:
                    data = json.load(json_file)
                # Title
                title = game_dir.name
                if "title" in data.keys():
                    title = data["title"]
                gid = create_gid(title)

                # Dev
                dev = None
                if "developer" in data.keys():
                    dev = data["developer"]
                # Year
                year = import_time
                if "year" in data.keys():
                    year = int(datetime(data["year"], 1, 1).timestamp())

                # Executable
                play_cmd = f'cd "{game_dir.path}" && python3 play.py'

                # Build game
                values = {
                    "source": source_id,
                    "added": year,
                    "name": title,
                    "game_id": gid,
                    "executable": play_cmd
                }
                if dev != None:
                    values["developer"] = dev
                game = Game(values)
                additional_data = {}
                cover_path = None
                for f in os.scandir(meta_path):
                    if not f.is_dir() and f.name.startswith("cover."):
                        cover_path = f.path
                        break
                if cover_path != None:
                    additional_data = {"local_image_path": Path(cover_path)}
                games.append((game, additional_data))

    return games

def create_gid(title:str) -> str:
    return title.encode('ascii', 'ignore').decode('ascii').replace(" ", "")