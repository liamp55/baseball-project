import random

glasnow_pitches = {'fastball': random.randint(95, 97), 'slider': random.randint(89, 91), 'curveball': random.randint(81, 85)}
kershaw_pitches = {'fastball': random.randint(88, 92), 'slider': random.randint(85, 88), 'curveball': random.randint(70, 74)}


print("Please select a pitcher")
pitcher_selection = input("Glasnow? or Kershaw?")
print("Please select a pitch type ")
pitches = ""
if pitcher_selection == "Glasnow":
    for i in list(glasnow_pitches.keys()):
        pitches += " " + i
    speed_selection = input(f"Enter a pitch:{pitches} ")

if pitcher_selection == "Kershaw":
    for i in list(kershaw_pitches.keys()):
        pitches += " " + i
    speed_selection = input(f"Enter a pitch:{pitches} ")

print("Pick a location for the pitch")
pitch_location = {
    1: "high and inside",
    2: "high and outside",
    3: "high",
    4: "low",
    5: "low and inside",
    6: "low and outside"
}
pitch_location_string = ""
pitch_location_keys = list(pitch_location.keys())
pitch_location_values = list(pitch_location.values())
for i in range(len(list(pitch_location))):
    pitch_location_string += str(pitch_location_keys[i]) + "." + str(pitch_location_values[i]) + " "
pitch_location_selection = int(input(pitch_location_string))





def create_strike_zone(ball):

    for j in range(0, 10):
        for i in range(0, 10):



create_strike_zone(1)


