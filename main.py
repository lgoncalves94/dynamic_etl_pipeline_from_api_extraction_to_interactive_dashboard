from weather_sense import WeatherSense

while True:
    choice = input("Read from file ? answer >yes<>no< to fetch current data >").lower()
    match choice:
        case 'yes':
             WeatherSense.main('yes') # Read from file
             break
        case 'no' :
            WeatherSense.main('no') # Fetch latest data
            break
        case _ :
            print('Answer with **yes** or **no** please ')


