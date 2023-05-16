count = int(input())
microbus = 0
truck = 0
train = 0
microbus_total = 0
truck_total = 0
train_total = 0

for i in range(count):
    weight = int(input())
    if weight <= 3:
        microbus += weight
        microbus_total += weight * 200
    elif 4 <= weight <= 11:
        truck += weight
        truck_total += weight * 175
    elif weight >= 12:
        train += weight
        train_total += weight * 120
    total = microbus + truck + train
    total_average = truck_total + train_total + microbus_total

average = total_average / total
microbus_percents = (microbus / total) * 100
truck_percents = (truck / total) * 100
train_percents = (train / total) * 100

print(f"{average:.2f}")
print(f"{microbus_percents:.2f}%")
print(f"{truck_percents:.2f}%")
print(f"{train_percents:.2f}%")


