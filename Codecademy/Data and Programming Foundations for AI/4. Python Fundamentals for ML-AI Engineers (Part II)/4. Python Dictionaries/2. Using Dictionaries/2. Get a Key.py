"""
Once you have a dictionary, you can access the values in it by providing the key. For example, let’s imagine we have a dictionary that maps buildings to their heights, in meters:

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

Copy to Clipboard

Then we can access the data in it like this:

print(building_heights["Burj Khalifa"]) # Prints 828
print(building_heights["Ping An"]) # Prints 599

Copy to Clipboard

Instructions
Checkpoint 1 Enabled
1.
We have provided a dictionary that maps the elements of astrology to the zodiac signs. Print out the list of zodiac signs associated with the "earth" element.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Print out the list of the "fire" signs.
"""
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])