from collections import ChainMap
from collections.abc import MutableMapping

# interface dla wielu słowników na raz

# print(issubclass(ChainMap, MutableMapping))
#
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4, "d": 5}
#
# chain_map = ChainMap(dict1, dict2)
#
# print(chain_map)
#
# dict1["a"] = 20
#
# print(chain_map)
#
# print(chain_map["a"])
# print(chain_map["b"])
# print(chain_map.maps)
#
# for key, value in chain_map.items():
#     print(key, value)


# stwórz config aplikacji

import os

default_config = {"theme": "Default", "language": "English", "show_ads": True}

env_config = os.environ

app_config = ChainMap(env_config, default_config)  # przy iteracji zwraca pierwsze wystąpienie ze słowników

user_config = {"theme": "Light Mode", "show_ads": False}

app_config = app_config.new_child(user_config) # daje na początek!! ostatni jest defaultowe

print(app_config)