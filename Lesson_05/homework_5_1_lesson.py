# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
car_data = {
    'Mercedes': {'color': 'silver', 'year': 2019, 'engine': 1.8, 'type': 'sedan', 'price': 50000},
    'Audi': {'color': 'black', 'year': 2020, 'engine': 2.0, 'type': 'sedan', 'price': 55000},
    'BMW': {'color': 'white', 'year': 2018, 'engine': 3.0, 'type': 'suv', 'price': 70000},
    'Lexus': {'color': 'gray', 'year': 2016, 'engine': 2.5, 'type': 'coupe', 'price': 45000},
    'Toyota': {'color': 'blue', 'year': 2021, 'engine': 1.6, 'type': 'hatchback', 'price': 25000},
    'Honda': {'color': 'red', 'year': 2017, 'engine': 1.5, 'type': 'sedan', 'price': 30000},
    'Ford': {'color': 'green', 'year': 2019, 'engine': 2.3, 'type': 'suv', 'price': 40000},
    'Chevrolet': {'color': 'purple', 'year': 2020, 'engine': 1.4, 'type': 'hatchback', 'price': 22000},
    'Nissan': {'color': 'pink', 'year': 2018, 'engine': 1.8, 'type': 'sedan', 'price': 35000},
    'Volkswagen': {'color': 'brown', 'year': 2021, 'engine': 1.4, 'type': 'hatchback', 'price': 28000},
    'Hyundai': {'color': 'gray', 'year': 2019, 'engine': 1.6, 'type': 'suv', 'price': 32000},
    'Kia': {'color': 'white', 'year': 2020, 'engine': 2.0, 'type': 'sedan', 'price': 28000},
    'Volvo': {'color': 'silver', 'year': 2017, 'engine': 1.8, 'type': 'suv', 'price': 45000},
    'Subaru': {'color': 'blue', 'year': 2018, 'engine': 2.5, 'type': 'wagon', 'price': 35000},
    'Mazda': {'color': 'red', 'year': 2019, 'engine': 2.5, 'type': 'sedan', 'price': 32000},
    'Porsche': {'color': 'black', 'year': 2017, 'engine': 3.0, 'type': 'coupe', 'price': 80000},
    'Jeep': {'color': 'green', 'year': 2021, 'engine': 3.0, 'type': 'suv', 'price': 50000},
    'Chrysler': {'color': 'gray', 'year': 2016, 'engine': 2.4, 'type': 'sedan', 'price': 22000},
    'Dodge': {'color': 'yellow', 'year': 2020, 'engine': 3.6, 'type': 'suv', 'price': 40000},
    'Ferrari': {'color': 'red', 'year': 2019, 'engine': 4.0, 'type': 'coupe', 'price': 500000},
    'Lamborghini': {'color': 'orange', 'year': 2021, 'engine': 5.0, 'type': 'coupe', 'price': 800000},
    'Maserati': {'color': 'blue', 'year': 2018, 'engine': 4.7, 'type': 'coupe', 'price': 100000},
    'Bugatti': {'color': 'black', 'year': 2020, 'engine': 8.0, 'type': 'coupe', 'price': 2000000},
    'McLaren': {'color': 'yellow', 'year': 2017, 'engine': 4.0, 'type': 'coupe', 'price': 700000},
    'Rolls-Royce': {'color': 'white', 'year': 2019, 'engine': 6.8, 'type': 'sedan', 'price': 500000},
    'Bentley': {'color': 'gray', 'year': 2020, 'engine': 4.0, 'type': 'coupe', 'price': 300000},
    'Jaguar': {'color': 'red', 'year': 2016, 'engine': 2.0, 'type': 'suv', 'price': 40000},
    'Land Rover': {'color': 'green', 'year': 2018, 'engine': 3.0, 'type': 'suv', 'price': 60000},
    'Tesla': {'color': 'silver', 'year': 2020, 'engine': 0.0, 'type': 'sedan', 'price': 60000},
    'Acura': {'color': 'white', 'year': 2017, 'engine': 2.4, 'type': 'suv', 'price': 40000},
    'Cadillac': {'color': 'black', 'year': 2019, 'engine': 3.6, 'type': 'suv', 'price': 55000},
    'Infiniti': {'color': 'gray', 'year': 2018, 'engine': 2.0, 'type': 'sedan', 'price': 35000},
    'Lincoln': {'color': 'white', 'year': 2021, 'engine': 2.0, 'type': 'suv', 'price': 50000},
    'GMC': {'color': 'blue', 'year': 2016, 'engine': 1.5, 'type': 'pickup', 'price': 30000},
    'Ram': {'color': 'black', 'year': 2019, 'engine': 5.7, 'type': 'pickup', 'price': 40000},
    'Chevy': {'color': 'red', 'year': 2017, 'engine': 2.4, 'type': 'pickup', 'price': 35000},
    'Dodge Ram': {'color': 'white', 'year': 2020, 'engine': 3.6, 'type': 'pickup', 'price': 45000},
    'Ford F-Series': {'color': 'gray', 'year': 2021, 'engine': 3.5, 'type': 'pickup', 'price': 50000},
    'Nissan Titan': {'color': 'silver', 'year': 2018, 'engine': 5.6, 'type': 'pickup', 'price': 35000}
}

search_criteria = (2017, 1.6, 36000)
min_year, min_engine, max_price = search_criteria
filtered = [
    (brand, data) for brand, data in car_data.items()
    if data['year'] >= min_year and data['engine'] >= min_engine and data['price'] <= max_price
]
sorted_cars = sorted(filtered, key=lambda x: x[1]['price'])
for brand, data in sorted_cars[:5]:
    print(f"{brand}: Color={data['color']}, Year={data['year']}, Engine={data['engine']}, "
          f"Type={data['type']}, Price={data['price']}")