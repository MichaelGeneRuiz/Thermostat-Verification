# Thermostat-Verification

## Introduction
Initially, I was inspired to start this project because my parents had complained that the thermostat never seemed to be accurate. Although it said it was, for example, 73 degrees, they claimed that sometimes it felt much colder. They had mused that maybe the temperature the thermostat was using was not the temperature of the living room, but another room of the house. This piqued my interest, and I felt that I should test whether the temperature and humidity of the living room was accurately portrayed by the thermostat.

## Setup
For this project, I used a Raspberry Pi 400, a breadboard, a 10 kOhm resistor, and a DHT22 sensor. I set up a circuit using all of these components, and a picture of the setup can be seen here: 

https://imgur.com/a/GIVq5uZ

With everything hooked up to the Raspberry Pi, I set out to create the script that I would use to take the readings. I first downloaded AdaFruit's DHT sensor library (the DHT22.py file in this repo is from that library) so that I could interface with the sensor. I then wrote the script that I would use to log the data taken from the sensor. The script (DataLogging.py), records the date and time, and then the humidity and temperature of the room ten times. This data is then written to a text file called logfile.txt. 

With the script finished, I needed a way to constantly execute it. For this purpose, I used cron, with which I scheduled the script to be run at the 0th minute of every hour. The crontab configuration can be seen here:

https://imgur.com/a/Bzjqb7D

All that was left to do was find a spot for the Raspberry Pi and accompanying circuit, and I was all set.

## Recording Data

While the Raspberry Pi dealth with the sensor readings, I needed a way to record the thermostat data as well. Luckily for me, my mom works from home! She had graciously volunteered to record the temperature and humidity readings from the thermostat whenever she could. This would provide me with the data I needed to compare to the readings from the DHT22.

## Parsing the Data

The final measurements were taken from the DHT22 at 8:00pm on 01/30/2022. The logfile produced on the Raspberry Pi was approximately 4500 lines, and the information was pretty unreadable. I could have formatted the initial logfile in a more legible manner, but hindsight is 20/20. However, I wrote a script (TextParsing.py) to transform the bulky, hard to understand text into a CSV file (logfile.csv) which could be viewed in Microsoft Excel. This made it much easier to understand and read the data that was produced by the DHT22.

## Understanding the Data and Conclusions

The CSV file is grouped in batches of 10, with the date, time, temperature, and humidity all in their respective columns. From the time we started, at 01/24/2022 at 8:15pm, to 01/30/2022 at 8:00pm, the DHT22 took readings every hour. When compared to the thermostat readings that my mom took (Thermostat Readings.txt), it is clear that the DHT22 produced similar results to the thermostat for the temperature readings. However, the humidity readings were often different by a decent margin (sometimes up to a 5% difference was recorded). 

This, at least, provides some evidence that there IS a difference between how the room feels and the readings on the thermostat. However, if this is the reason that the room allegedly feels much colder than the temperature implies is unknown. After all, a 5% difference in humidity shouldn't make too much of a difference in a room's feel, at least in my opinion.
