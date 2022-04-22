
import time
import random
from typing import Any

from catanatron.state_functions import (
    get_longest_road_length,
    get_played_dev_cards,
    get_player_buildings,
    player_key,
    player_num_dev_cards,
    player_num_resource_cards,
)
from catanatron.game import Game
from catanatron.models.player import Player
from catanatron.models.actions import ActionType
from catanatron.models.enums import RESOURCES, BuildingType
from catanatron_gym.features import (
    build_production_features,
    reachability_features,
    resource_hand_features,
)
from catanatron_experimental.machine_learning.players.tree_search_utils import (
    expand_spectrum,
)

from catanatron import Player
from catanatron_experimental.cli.cli_players import register_player

import random

from catanatron.state_functions import (
    player_key,
)
from catanatron.models.player import Player
from catanatron.game import Game


@register_player("Human")
class HumanPlayer(Player):
    def decide(self, game, playable_actions):
        for i, action in enumerate(playable_actions):
            print(f"{i}: {action.action_type} {action.value}")
        i = None
        while i is None or (i < 0 or i >= len(playable_actions)):
            print("Please enter a valid index:")
            try:
                x = input(">>> ")
                i = int(x)
            except ValueError:
                pass

        return playable_actions[i]