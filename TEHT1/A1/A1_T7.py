print(" Fuel consumption calculator")
feed = input("Enter travel distance(kilometers):")
distance = int(feed)

feed = input("Enter fuel usage(liters):")
FuelUsage = int(feed)

consumption = (FuelUsage/distance)*100
consumption =int(consumption)

print(f"Fuel consumption is {consumption} l per 100 km”")