import json
import random
from pprint import pprint
with open('IndianJson.json', 'r') as indian_data:
    data = json.load(indian_data)


STATE_IMAGE = {}
for state in data['States']:
    if state["StateName"] in ["Maharashtra", "Madhya Pradesh", "Manipur", "Meghalaya", "Karnataka", "Kerala", "Mizoram",
                              "Nagaland", "Odisha","Andhra Pradesh", "Arunachal Pradesh","Assam","Bihar", "Chhattisgarh",
                              "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand",
                              "Daman and Diu", "Ladakh", "Rajasthan", "Punjab", "Sikkim", "Tamil Nadu", "Telangana",
                              "Tripura", "West Bengal", "Uttar Pradesh", "Uttarakhand"]:
        state_images = state['StateImage']
        alternative_images = [image for i, image in enumerate(state_images) if i % 2 == 0]
        for stateimage in alternative_images:
            STATE_IMAGE[state["StateName"]] = stateimage.split(".")[0]

CITY_IMAGE = {}
BEST_SELLER = {}
for state in data['States']:
    if state["StateName"] in ["Maharashtra", "Madhya Pradesh", "Manipur", "Meghalaya", "Karnataka", "Kerala", "Mizoram",
                              "Nagaland", "Odisha","Andhra Pradesh", "Arunachal Pradesh","Assam","Bihar", "Chhattisgarh",
                              "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand",
                              "Daman and Diu", "Ladakh", "Rajasthan", "Punjab", "Sikkim", "Tamil Nadu", "Telangana",
                              "Tripura", "West Bengal", "Uttar Pradesh", "Uttarakhand"]:
        for city in state["Cities"]:
            city_image = city["CityImage"]
            IdealLengthOfTrip = city['IdealLengthOfTrip']
            CityName = city["CityName"]
            alternative_images = [image for i, image in enumerate(city_image) if i % 2 == 0]
            for cityimage in alternative_images:
                CITY_IMAGE[city["CityName"]] = cityimage.split(".")[0]
                BEST_SELLER_TITLE = CityName + " " + IdealLengthOfTrip
                BEST_SELLER[BEST_SELLER_TITLE] = cityimage.split(".")[0]


SPOT_IMAGE = {}

for state in data['States']:
    if state["StateName"] in ["Maharashtra", "Madhya Pradesh", "Manipur", "Meghalaya", "Karnataka", "Kerala", "Mizoram",
                              "Nagaland", "Odisha","Andhra Pradesh", "Arunachal Pradesh","Assam","Bihar", "Chhattisgarh",
                              "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand",
                              "Daman and Diu", "Ladakh", "Rajasthan", "Punjab", "Sikkim", "Tamil Nadu", "Telangana",
                              "Tripura", "West Bengal", "Uttar Pradesh", "Uttarakhand"]:
        for city in state["Cities"]:
            for spot in city.get("TouristSpots", []):
                # Check if 'Images' key exists in the current spot dictionary
                if 'Images' in spot:
                    spot_image = spot["Images"]
                    alternative_images = [image for i, image in enumerate(spot_image) if i % 2 == 0]
                    for spotimage in alternative_images:
                        # Check if 'TouristSpotName' key exists in the current spot dictionary
                        if 'TouristSpotName' in spot:
                            SPOT_IMAGE[spot["TouristSpotName"]] = spotimage.split(".")[0]
                        else:
                            print("Warning: 'TouristSpotName' not found in spot:", spot)
                else:
                    print("Warning: 'Images' not found in spot:", spot)


UT_IMAGE = {}
for ut in data["UnionTerritory"]:
    if ut['UnionTerritoryName'] in ["Delhi", "Lakshadweep", "Puducherry", "Dadra and Nagar Haveli",
                                    "Chandigarh", "Andaman and Nicobar Islands"]:
        ut_images = ut["UnionTerritoryImage"]
        alternative_images = [image for i, image in enumerate(ut_images) if i % 2 == 0]
        for images in alternative_images:
            UT_IMAGE[ut["UnionTerritoryName"]] = images.split(".")[0]

BEST_SELLER_10 = dict(random.sample(list(BEST_SELLER.items()), 10))
BEST_SELLER_10 = dict(BEST_SELLER_10)



SPOT_IMAGE_10 = dict(random.sample(list(SPOT_IMAGE.items()), 10))
SPOT_IMAGE_10 = dict(SPOT_IMAGE_10)

CITY_IMAGE_10 = random.sample(list(CITY_IMAGE.items()), 10)
CITY_IMAGE_10 = dict(CITY_IMAGE_10)

STATE_IMAGE_10 = random.sample(list(STATE_IMAGE.items()), 9)
STATE_IMAGE_10 = dict(STATE_IMAGE_10)

UT_IMAGE_10 = random.sample(list(UT_IMAGE.items()), 3)
UT_IMAGE_10 = dict(UT_IMAGE_10)


