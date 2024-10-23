class Car:
    def __init__(self, cars):
        self._cars = cars
        self._idx = 0

    def __iter__(self):
        # return iter(self._cars)
        return self  # najczęstsza implementacja

    def __next__(self):
        if self._idx >= len(self._cars):
            raise StopIteration

        result = self._cars[self._idx]
        self._idx += 1
        return result


# for car in Car(["tico", "bmw", "fiat"]):
#     print(car)

cars = Car(["tico", "bmw", "fiat"])

# print(next(cars))
# print(next(cars))
# print(next(cars))
# print(next(cars))


continents = {
    "africa": {
        "egypt": "cairo",
        "libya": "tripoli",
        "nigeria": "abuja",
        "south_africa": "pretoria",
        "kenya": "nairobi",
        "morocco": "rabat"
    },
    "europe": {
        "germany": "berlin",
        "poland": "warsaw",
        "france": "paris",
        "spain": "madrid",
        "italy": "rome",
        "united_kingdom": "london"
    },
    "asia": {
        "china": "beijing",
        "india": "new_delhi",
        "japan": "tokyo",
        "south_korea": "seoul",
        "indonesia": "jakarta",
        "saudi_arabia": "riyadh"
    },
    "north_america": {
        "united_states": "washington_dc",
        "canada": "ottawa",
        "mexico": "mexico_city",
        "cuba": "havana",
        "jamaica": "kingston",
        "panama": "panama_city"
    },
    "south_america": {
        "brazil": "brasilia",
        "argentina": "buenos_aires",
        "chile": "santiago",
        "colombia": "bogota",
        "peru": "lima",
        "venezuela": "caracas"
    },
    "australia": {
        "australia": "canberra",
        "new_zealand": "wellington",
        "fiji": "suva",
        "papua_new_guinea": "port_moresby",
        "samoa": "apia"
    },
    "antarctica": {
        "research_station_1": "amundsen_scott_station",
        "research_station_2": "mcmurdo_station"
    }
}


class CapitalsIterator:
    def __init__(self, capitals):
        self._capitals = capitals
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._capitals):
            raise StopIteration

        capital = self._capitals[self._idx]
        self._idx += 1
        return capital


class Capitals:
    def __init__(self, continents_):
        self._continents = continents_

    def __iter__(self):
        capitals = []
        for countries in self._continents.values():
            capitals.extend(countries.values())

        capitals.sort()
        return CapitalsIterator(capitals)


capitals_ = Capitals(continents_=continents)

for capital in capitals_:
    print(capital)

# class Continents:
#     def __init__(self, continents):
#         self._continents = continents
#         self._idx = 0
#
#     def __iter__(self):
#         # return iter(self._cars)
#         return self  # najczęstsza implementacja
#
#     def __next__(self):
#         # if self._idx >= len(self._cars):
#         #     raise StopIteration
#
#         capitals = []
#
#         for continent in self._continents:
#             for country, capital in self._continents[continent].items():
#                 capitals.append(capital)
#
#         sorted_capitals = sorted(capitals)
#
#         if self._idx >= len(capitals):
#             raise StopIteration
#
#         result = sorted_capitals[self._idx]
#         self._idx += 1
#         return result

#
# con = Continents(continents)
#
#
# print(next(con))
# print(next(con))
# print(next(con))
# print(next(con))
# print(next(con))
# print(next(con))
