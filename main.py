mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

print("Total number of missions " + str(len(mission_names)))

success_count = 0
for i in range(len(mission_success)):
    if mission_success[i]:
        success_count += 1
print("Number  of sucessful missions" + str(success_count))


success_rate = (success_count / len(mission_names)) * 100
print(f"Success rate: {success_rate:.2f}%")

print("Missions launched before the year 2000:")
for i in range(len(mission_years)):
    if mission_years[i] < 2000:
        print("- " + mission_names[i])