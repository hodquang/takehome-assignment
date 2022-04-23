import json
from datetime import datetime
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def getTimeZoneArray(name, targetTime, loc):
    # get dict of userID:city from json
    file = open(name)
    setarray = set([])
    data = json.load(file)
    print(len(data))
    # usercount= 0;
    for userID in data:
        # usercount += 1
        # print(usercount)
        for info in data[userID]:
            array = info.split(',');
            geolocator = Nominatim(user_agent="geoapiExercises")
            try:
                if (array[1] != "None"):
                    location = geolocator.geocode(array[1].strip())
                    region = TimezoneFinder().timezone_at(lng=location.longitude, lat=location.latitude)

                    follower_timezone = pytz.timezone(region)
                    user_timezone = pytz.timezone(loc)

                    follower_timestamp = follower_timezone.localize(targetTime)
                    user_timestamp = follower_timestamp.astimezone(user_timezone)

                    setarray.add(user_timestamp)
            except Exception as e:
                print('')
                # print("Wrong location provided for " + userID)
                # print("Wont be added into dict")

    file.close()
    return setarray

if __name__ == '__main__':
    print("What is your location?")
    region = "US/Eastern"
    print("Select a time that you would like to post your tweets worldwide in their timezone: ")
    # 0-24 hours time
    time = datetime(2022, 4, 25,7)
    print(getTimeZoneArray("test.json",time, region))




