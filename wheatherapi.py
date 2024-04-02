import requests

def weatherapi(cityname):
   city=cityname

   base_url="https://api.openweathermap.org/data/2.5/weather"
   api_key="981b7c620ea4aa4fb4eb08f8d9b88d65"

   A={
     "q":city,
     "appid":api_key,
     "units":"metric"
     }

   respond=requests.get(base_url,A)
   data=respond.json()
   print(data)
   weather_info = {
     'lon': data['coord']['lon'],
     'lat': data['coord']['lat'],
     'temp': data['main']['temp'],
     'description': data['weather'][0]['description'],
     'name': data['name']
    }
   return weather_info


def temperature_city(cityname):
  city=cityname

  base_url="https://api.openweathermap.org/data/2.5/weather"
  api_key="981b7c620ea4aa4fb4eb08f8d9b88d65"

  A={
    "q":city,
    "appid":api_key,
    "units":"metric"
    }

  respond=requests.get(base_url,A)
  data=respond.json()
  
  weather_info = {
    'lon': data['coord']['lon'],
    'lat': data['coord']['lat'],
    'name': data['name']
  }
  # print(weather_info)
  return weather_info
def get_city_coordinates(cities):
    city_coordinates = {}  # Dictionary to store city coordinates and counts

    # Iterate through each city in the list
    for city_name in cities:
        # Fetch latitude, longitude, and name for the city using temperature_city function
        city_data = temperature_city(city_name)
        city_lat = city_data['lat']
        city_lon = city_data['lon']
        city_actual_name = city_data['name']

        # Check if the city is already in the dictionary
        if city_actual_name in city_coordinates:
            # Increment the count for the city
            city_coordinates[city_actual_name]['count'] += 1
        else:
            # Add the city to the dictionary with initial count and coordinates
            city_coordinates[city_actual_name] = {'lat': city_lat, 'lon': city_lon, 'count': 1}

    print(city_coordinates) 
    return city_coordinates


# Example list of cities
# cities = ['Mumbai', 'Panvel', 'Ranchi', 'Surat', 'Hyderabad', 'Panvel','Mumbai', 'Panvel', 'Ranchi', 'Surat', 'Hyderabad', 'Panvel']

# # Get coordinates for each city
# city_coordinates = get_city_coordinates(cities)



# Print the dictionary containing city coordinates
# for city, coordinates in city_coordinates.items():
#     print(f"City: {city}, Latitude: {coordinates['latitude']}, Longitude: {coordinates['longitude']}")
