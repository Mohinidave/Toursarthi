import json
import random

#  Reading json file
with open('IndianJson.json', 'r') as file:
    json_data = json.load(file)
#  Empty list 
Spot_all_info=[]
cities_in_state=[]
# it is used to extact info of particular city(target_city) from json 
def extract_city_info(json_data, target_city):
    for state in json_data.get('States', []):
        for city in state.get('Cities', []):
            if city.get('CityName') == target_city:
                city_info = {
                    'CityName': city.get('CityName'),
                    'CityImage': city.get('CityImage'),
                    'CityDescription': city.get('CityDescription'),
                    'Category': city.get('Category'),
                    'BestMonthToVisit': city.get('BestMonthToVisit'),
                    'IdealLengthOfTrip': city.get('IdealLengthOfTrip'),
                    'Budgets': city.get('Budget')
                }
                # print(city_info)
                return city_info
    print(f"City '{target_city}' not found.")

# Thakur College of science and commerce

# it is used to extact info of particular citie's touristspot from json 
def extract_tourist_spot_info_with_city(json_data, target_city, target_spot):
    for state in json_data.get('States', []):
        for city in state.get('Cities', []):
            if city.get('CityName') == target_city:
                for spot in city.get('TouristSpots', []):
                    if spot.get('TouristSpotName') == target_spot:
                        spot_info = {
                            'TouristSpotName': spot.get('TouristSpotName'),
                            'Images': spot.get('Images'),
                            'ReasonOfPopularity': spot.get('ReasonOfPopularity'),
                            'OpeningTime': spot.get('OpeningTime'),
                            'ClosingTime': spot.get('ClosingTime'),
                            'EntryFee': spot.get('EntryFee'),
                            'BestHourToVisit': spot.get('BestHourToVisit'),
                            'Location': spot.get('Location'),
                            'ThingsToDo': spot.get('ThingsToDo'),
                            'NearestRailway': spot.get('Nearestrailway'),
                            'NearestAirport': spot.get('NearestAirport'),
                            'Description': spot.get('Description')
                        }
                        # print(spot_info)
                        return (spot_info)
    print(f"Tourist spot '{target_spot}' in city '{target_city}' not found.")

# extract_tourist_spot_info(json_data,"Mumbai","Marine Drive")

# It will extract touristspot info from its name
def extract_tourist_spot_info(json_data, target_spot):
    for state in json_data.get('States', []):
        for city in state.get('Cities', []):
            for spot in city.get('TouristSpots', []):
                if spot.get('TouristSpotName') == target_spot:
                    spot_info = {
                        'TouristSpotName': spot.get('TouristSpotName'),
                        'Images': spot.get('Images'),
                        'ReasonOfPopularity': spot.get('ReasonOfPopularity'),
                        'OpeningTime': spot.get('OpeningTime'),
                        'ClosingTime': spot.get('ClosingTime'),
                        'EntryFee': spot.get('EntryFee'),
                        'BestHourToVisit': spot.get('BestHourToVisit'),
                        'Location': spot.get('Location'),
                        'NearestRailway':spot.get('NearestRailway'),
                        'ThingsToDo': spot.get('ThingsToDo'),
                        'NearestAirport': spot.get('NearestAirport'),
                        'Description': spot.get('Description')
                    }
                    # print(spot_info)
                    return spot_info
    print(f"Tourist spot '{target_spot}' not found.")
    return None
# extract_tourist_spot_info(json_data,"Marine Drive")
# it is used to extact info of particular state from json 
def extract_state_info(json_data, target_state):
    for state in json_data.get('States', []):
        if state.get('StateName') == target_state:
            state_info = {
                'StateId': state.get('StateId'),
                'StateName': state.get('StateName'),
                'StateImage': state.get('StateImage'),
                'StateDescription': state.get('StateDescription')
            }
            # print(state_info)
            return state_info
    print(f"State '{target_state}' not found.")



# it is used to extact info of particular state's cities from json 
def extract_cities_in_state(json_data, target_state):
    for state in json_data.get('States', []):
        if state.get('StateName') == target_state:
            cities = state.get('Cities', [])
            if cities:
                for city in cities:
                    city_info = {
                        'CityId': city.get('CityId'),
                        'CityName': city.get('CityName'),
                        'CityImage': city.get('CityImage'),
                        'CityDescription': city.get('CityDescription'),
                        'BestMonthToVisit': city.get('BestMonthToVisit'),
                        'Budgets': city.get('Budgets'),
                        'Category': city.get('Category'),
                        'IdealLengthOfTrip': city.get('IdealLengthOfTrip')
                    }
                cities_in_state.append(city_info['CityName'])
                
                return cities_in_state
            else:
                print(f"No cities found in the state '{target_state}'.")
                return
    print(f"State '{target_state}' not found.")
state=extract_cities_in_state(json_data,"Goa")
print("cities in that State",state)
# it is used to extact info of particular citie's touristspot from json 
def extract_tourist_spots_in_city(json_data, target_city):
    for state in json_data.get('States', []):
        for city in state.get('Cities', []):
            if city.get('CityName') == target_city:
                tourist_spots = city.get('TouristSpots', [])
                if tourist_spots:
                    for spot in tourist_spots:
                        spot_info = {
                            'TouristSpotName': spot.get('TouristSpotName'),
                            'Images': spot.get('Images'),
                            'ReasonOfPopularity': spot.get('ReasonOfPopularity'),
                            'OpeningTime': spot.get('OpeningTime'),
                            'ClosingTime': spot.get('ClosingTime'),
                            'EntryFee': spot.get('EntryFee'),
                            'BestHourToVisit': spot.get('BestHourToVisit'),
                            'Location': spot.get('Location'),
                            'ThingsToDo': spot.get('ThingsToDo'),
                            'NearestRailway': spot.get('NearestRailway'),
                            'NearestAirport': spot.get('NearestAirport'),
                            'Description': spot.get('Description')
                        }
                        # print(spot_info)
                        Spot_all_info.append(spot_info)
            
                    return Spot_all_info
                else:
                    print(f"No tourist spots found in the city '{target_city}'.")
                    return
    print(f"City '{target_city}' not found.")

def extract_random_tourist_spots_in_city(json_data, target_city):
    for state in json_data.get('States', []):
        for city in state.get('Cities', []):
            if city.get('CityName') == target_city:
                tourist_spots = city.get('TouristSpots', [])
                if tourist_spots:
                    all_spot_names = [spot.get('TouristSpotName') for spot in tourist_spots]
                    # Randomly select 20 Tourist Spot names
                    selected_spot_names = random.sample(all_spot_names, min(20, len(all_spot_names)))
                    return selected_spot_names
                else:
                    print(f"No tourist spots found in the city '{target_city}'.")
                    return
    print(f"City '{target_city}' not found.")
    return None



def extract_cities_in_state_list(json_data, target_state):
    for state in json_data.get('States', []):
        if state.get('StateName') == target_state:
            cities = state.get('Cities', [])
            if cities:
                city_names = [city.get('CityName') for city in cities]
                return city_names
            else:
                return []
    return []

def extract_unionterritory_info(json_data, target_ut_name):
    union_territories = json_data.get('UnionTerritory', [])

    for ut in union_territories:
        if ut.get('UnionTerritoryName') == target_ut_name:
            ut_info = {
                'UnionTerritoryName': ut.get('UnionTerritoryName'),
                'UnionTerritoryDescription': ut.get('UnionTerritoryDescription'),
                'BestMonthToVisit': ut.get('BestMonthToVisit'),
                'Area': ut.get('Area'),
                'Population': ut.get('Population'),
                'OfficialLanguage': ut.get('OfficialLanguage')
            }
            return ut_info

    print(f"Union Territory '{target_ut_name}' not found.")
    return None
# target_ut_name = 'Chandigarh'
# ut_info = extract_unionterritory_info(json_data, target_ut_name)


def extract_tourist_spots_by_ut_name(json_data, target_ut_name):
    union_territories = json_data.get('UnionTerritory', [])

    for ut in union_territories:
        if ut.get('UnionTerritoryName') == target_ut_name:
            tourist_spots = ut.get('TouristSpots', [])
            if tourist_spots:
                ut_tourist_spots = []
                for spot in tourist_spots:
                    tourist_spot_info = {
                        'TouristSpotName': spot.get('TouristSpotName'),
                        'Images': spot.get('Images'),
                        'ReasonOfPopularity': spot.get('ReasonOfPopularity'),
                        'OpeningTime': spot.get('OpeningTime'),
                        'ClosingTime': spot.get('ClosingTime'),
                        'EntryFee': spot.get('EntryFee'),
                        'BestHourToVisit': spot.get('BestHourToVisit'),
                        'Location': spot.get('Location'),
                        'ThingsToDo': spot.get('ThingsToDo'),
                        'NearestRailway': spot.get('NearestRailway'),
                        'NearestAirport': spot.get('NearestAirport'),
                        'Description': spot.get('Description')
                    }
                    ut_tourist_spots.append(tourist_spot_info['TouristSpotName'])

                return ut_tourist_spots

    print(f"Union Territory '{target_ut_name}' not found.")
    return None

# Example usage
target_ut_name = 'Andaman and Nicobar Islands'
ut_tourist_spots = extract_tourist_spots_by_ut_name(json_data, target_ut_name)

# print(ut_tourist_spots)
def extract_union_territory_names(json_data):
    union_territories = json_data.get('UnionTerritory', [])
    ut_names = [ut.get('UnionTerritoryName') for ut in union_territories]
    return ut_names


# union_territory_names = extract_union_territory_names(json_data)

# print("Union Territory Names:")
# for ut_name in union_territory_names:
#     print(ut_name) 



def extract_random_tourist_spot_names_in_state(json_data, target_state_name):
    states = json_data.get('States', [])

    for state in states:
        if state.get('StateName') == target_state_name:
            cities = state.get('Cities', [])
            all_tourist_spot_names = []

            for city in cities:
                tourist_spots = city.get('TouristSpots', [])

                for spot in tourist_spots:
                    spot_name = spot.get('TouristSpotName')
                    all_tourist_spot_names.append(spot_name)

            # Randomly select 20 Tourist Spot names
            selected_tourist_spot_names = random.sample(all_tourist_spot_names, min(20, len(all_tourist_spot_names)))

            return selected_tourist_spot_names

    print(f"State '{target_state_name}' not found.")
    return None

random_tourist_spot_names = extract_random_tourist_spot_names_in_state(json_data, "Goa")
print(random_tourist_spot_names)

