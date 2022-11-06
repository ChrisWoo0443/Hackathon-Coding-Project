import re

f = open("dailyValues.txt", "r")

total_avg = 0.0
bathroom_avg = 0.0
drink_avg = 0.0
shower_avg = 0.0
sink_avg = 0.0
dishes_avg = 0.0
laundry_avg = 0.0
gardening_avg = 0.0 

days = 0

bathroom_count = 0
drink_count = 0
shower_count = 0
sink_count = 0
dishes_count = 0
laundry_count = 0
gardening_count = 0

total_value = 0
bathroom_value = 0
drink_value = 0
shower_value = 0
sink_value = 0
dishes_value = 0
laundry_value = 0
gardening_value = 0

#Parses through the text file and calculates the average amount of water used by each of the possible methods and tracks the amount of times they do so

for line in f:
    line = line.rstrip()
    
    if line == "":
        continue
    if line.endswith("gallons"): 
        days += 1
        numbers = re.findall('[0-9]+', str(line))
        number = int(numbers[0])
        current_total = number
        total_value += number
    if line.startswith("bathroom"):
        numbers = re.findall('[0-9]+', str(line))
        number = int(numbers[0])
        bathroom_count += number
        bathroom_value += number * 1.6
    if line.startswith("drink"):
        numbers = re.findall('[0-9]+', str(line))
        number = int(numbers[0])
        drink_count += number
        drink_value += number * 0.1320312
    if line.startswith("shower"):
        numbers = re.findall('[0-9]+', str(line))
        number = int(numbers[0])
        shower_count += number
        shower_value += number * 17
    if line.startswith("sink"):
        numbers = re.findall('[0-9]+', str(line))
        number = int(numbers[0])
        sink_count += number
        sink_value += number * 0.22
    if line.startswith("dishes"):
        numbers = re.findall('[0-9]+', str(line))
        number = int(numbers[0])
        dishes_count += number
        dishes_value += number * 6
    if line.startswith("laundry"):
        numbers = re.findall('[0-9]+', str(line))
        number = int(numbers[0])
        laundry_count += number
        laundry_value += number * 20
    if line.startswith("gardening"):
        numbers = re.findall('[0-9]+', str(line))
        number = int(numbers[0])
        gardening_count += number
        gardening_value += number * 62.3



drink_difference = 1 - drink_avg
total_use_diff = 108 - total_avg


total_avg += total_value/days
bathroom_avg += bathroom_value/days 
drink_avg += drink_value/days
shower_avg += shower_value/days
sink_avg += sink_value/days
dishes_avg += dishes_value/days
laundry_avg += laundry_value/days
gardening_avg += gardening_value/days


f.close()


print(f"You have been tracking your water use for {days} day(s) now. On average, you use {total_avg:.2f} gallons of water per day. Today you have used a total of {current_total} gallons today.\n")


print(f"You have used the bathrooom {bathroom_count} over the past {days} day(s). On average, you use {bathroom_avg:.2f} gallons of water per day.\n")
print(f"You have drank {drink_count} times in the past {days} day(s). On average, you drink {drink_avg:.2f} gallons of water per day.\n")

# Checks and reports whether the user has been drinking enough water
if drink_difference > 0:
    print(f"You should drink an extra {drink_avg:.2f} gallons per day.\n")
else:
    print("Great job! You are drinking a healthy amount of water per day.\n")

print(f"You have showered {shower_count} times over the past {days} day(s). On average, you use {shower_avg:.2f} gallons of water while showering per day.\n")
print(f"You have used the sink {sink_count} times over the past {days} day(s). On average, you use {sink_avg:.2f} gallons of water while using the sink per day.\n")
print(f"You have washed dishes {dishes_count} time(s) over the past {days} days. On average, you use {dishes_avg:.2f} gallons per day to wash your dishes at home.\n")
print(f"You have done laundry {laundry_count} times over the past {days} day(s). On average, you use {laundry_avg:.2f} gallons per day.\n")
print(f"You have watered your graden {gardening_count} time over the past {days} days. On average, you use {gardening_avg:.2f} gallons of water gardening per day.\n")

# Checks whether the user has been using too much water, if so, tells them by how much
if total_use_diff < 0:
    print("You should cut down your water use! You are using an extra", abs(total_use_diff),"gallons of water per day.\n")
else:
    print("Great job! You are using a good amount of water per day.\n")
