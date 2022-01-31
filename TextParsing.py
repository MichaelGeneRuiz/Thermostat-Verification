readfile = open("Logs/logfile.txt", 'r')
writefile = open("Logs/logfile.csv", 'w')

humidity_data = []
temperature_data = []
date_data = []
time_data = []

for line in readfile:
    
    if line == "\n":
        continue
    
    split_line = line.split()
    
    if split_line[0] == "Humidity":
        humidity_data.append(split_line[2])
    elif split_line[0] == "Temperature":
        temperature_data.append(split_line[2])
    else:
        date_data.append(split_line[0])
        time_data.append(split_line[1])

readfile.close()

count = 0

writefile.truncate(0)
writefile.write("Date,Time,Temperature,Humidity\n")

for i in range(len(date_data)):
    if i % 10 == 0 and i != 0:
        writefile.write("\n")

    writefile.write(date_data[i] + "," + time_data[i] + "," + temperature_data[i] + "," + humidity_data[i] + "\n")

writefile.close()
