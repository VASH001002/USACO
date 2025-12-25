import requests
import json
from datetime import datetime, timedelta
import os

best_weather = []
weather = []

class Friend:
  def __init__(self):
      self.name = input("\nEnter your friend's name: ")

      self.favorite_activities = []
      print(f"\nEnter {self.name}'s top 5 favorite activities:\n")

      for i in range(5):
          activity = input(f"Activity {i + 1}: ")
          self.favorite_activities.append(activity)




def find_weather(lat, lon):
    url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        forecast_url = weather_data.get("properties",{}).get("forecast") + "/hourly"
        print (f"Forecast URL: {forecast_url}")

        newresponse = requests.get(forecast_url)
        if newresponse.status_code == 200:
             forecast_data = newresponse.json()
#             print(forecast_data)

             forecast = forecast_data.get("properties", {})
             #print(forecast)



             forecast = forecast_data.get("properties", {}).get("periods", [])[:25]
             for period in forecast:
                 start_time = period.get('startTime', '')
                 day = start_time.split('T')[0]
                 hour = start_time.split('T')[1][:5]

                 weather_cur = [day, hour, period['temperature'], period['temperatureUnit'], period['shortForecast']]

                 weather.append(weather_cur)

        forecast_office = weather_data['properties']['forecastOffice']
        timezone = weather_data['properties']['timeZone']
        print(f"Forecast Office: {forecast_office}, Time Zone: {timezone}")


    else:
        print(f"Error fetching weather data: Status {response.status_code}")
        print(f"Response: {response.text}")
    
    return weather




# figure out a way to convert zipcode to lat, lon 
def get_coordinates(zipcode, country="US"):
  url = f"http://api.zippopotam.us/{country}/{zipcode}"
  response = requests.get(url)

  if response.status_code == 200:
      data = response.json()
      latitude = data['places'][0]['latitude']
      longitude = data['places'][0]['longitude']
      return latitude, longitude
  else:
      return None, None


def get_weather():
    zipcode = input("\nEnter your ZIP code - none of this is saved, just to find out the weather: ")
    lat, lon = get_coordinates(zipcode)
    find_weather(lat, lon)


def load_existing_schedule(filename="schedule.json"):
    """Load an existing schedule from a JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []

def create_schedule(existing_schedule=None):
    schedule = []  # If an existing schedule is passed, use it
    current_time = datetime.strptime("08:00 AM", "%I:%M %p")

    if not existing_schedule:
        print("Let's build your daily schedule starting from 8:00 AM.")
        print("You’ll be asked what you’re doing, when that ends, and whether it’s movable.")
        print("Type 'done' to finish at any time, or 'free' if you're free during a time.\n")

    while True:
        start_str = current_time.strftime("%I:%M %p")
        activity = input(f"What are you doing at {start_str}? (or type 'free'): ").strip()

        if activity.lower() == 'done':
            break

        if activity.lower() == 'free':
            label = 'Free time'
            movable = 'yes'  # Free time is assumed to be movable
        else:
            label = activity
            # Ask whether the activity is movable
            while True:
                movable = input(f"Is '{label}' movable? (yes/no): ").strip().lower()
                if movable in ['yes', 'no']:
                    break
                print("Please enter 'yes' or 'no'.")

        end_str = input(f"When does '{label}' end? (e.g., 09:30 AM): ").strip()
        if end_str.lower() == 'done':
            break

        try:
            end_time = datetime.strptime(end_str, "%I:%M %p")
        except ValueError:
            print("❌ Invalid time format. Please use something like 09:30 AM.\n")
            continue

        if end_time <= current_time:
            print("❌ End time must be after start time. Try again.\n")
            continue

        schedule.append({
            'start': start_str,
            'end': end_time.strftime("%I:%M %p"),
            'activity': label,
            'movable': movable
        })

        current_time = end_time

        # Optional: Automatically end at 10 PM
        if current_time.hour >= 22:
            print("You've reached 10:00 PM. Ending schedule.")
            break

    print("\n🗓️ Your final schedule:")
    for entry in schedule:
        status = "Movable" if entry['movable'] == 'yes' else "Not Movable"
        print(f"{entry['start']} - {entry['end']}: {entry['activity']} ({status})")

    return schedule

def save_schedule_json(schedule, filename="schedule.json"):
    """Save the schedule to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(schedule, file, indent=4)

    print(f"Schedule saved to {filename}")



def main():
    free_weather = []
    free_time = []
    movable_schedule = []
    get_weather()
    
    schedule_file = "schedule.json"
    existing_schedule = load_existing_schedule(schedule_file)

    if existing_schedule:
        print("Found an existing schedule. Loading it...\n")
        print("Would you like to modify the existing schedule? (y/n): ")
        modify_schedule = input().strip().lower()

        if modify_schedule == 'y':
            new_schedule = create_schedule(existing_schedule)
        else:
            new_schedule = existing_schedule
    else:
        print("No existing schedule found. Let's create a new one.\n")
        new_schedule = create_schedule()

    # Save the updated schedule
    save_schedule_json(new_schedule, schedule_file)
            
    for item in new_schedule:
        if item['movable'] == "yes":
            movable_schedule.append(item)

    # Match best weather with movable time slots
    print("\n📅 Finding the best time to go outside based on your free/movable slots and the weather...\n")

    
    for item in movable_schedule:
        
        time = item['start']
        time1 = item['end']
        if time[6:] == "PM":
            time = int(time[:2]) * 60 + 12*60 + int(time[3:5])
        else:
            time = int(time[:2]) * 60 + int(time[3:5])

        if time1[6:] == "PM":
            time1 = int(time1[:2]) * 60 + 12*60 + int(time1[3:5])
        else:
            time1 = int(time1[:2]) * 60 + int(time1[3:5])

        free_time.append([time, time1])

    for x in free_time:
        for y in weather:
            if x[0] <= int(y[1][:2]) * 60 + int(y[1][3:5]) < x[1]:
                free_weather.append(y)

    yod = sorted(free_weather, key=lambda x: x[2], reverse=True)

    print(f"Next best time to go outside: {yod[0][0]} at {yod[0][1]}")
    print(f"Temperature: {yod[0][2]}, {yod[0][3]}")
    print(f"Weather: {yod[0][4]}")


main()