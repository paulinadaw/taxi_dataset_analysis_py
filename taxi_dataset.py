from read_data import ReadData

taxi_dataset = ReadData("taxi_dataset.csv")

# 1. Display data from a CSV file
# print(taxi_dataset.data)


# 2. What information does the dataset contain?
print(f"\nThe dataset column names: {taxi_dataset.column_names}")


# 3. Taxi companies in Chicago
taxi_dataset_companies = taxi_dataset.display_column_data("company")

taxi_companies = list(set(taxi_dataset_companies))
taxi_companies.sort()

print(f"\nTaxi service providers: {taxi_companies}")
print(f"\nThe number of taxi companies included in the file: {len(taxi_companies)}")


# 4. The frequency of occurrence of particular taxi companies in the file
taxi_companies_ranking = {}

for company in taxi_dataset_companies:
    if company != "No value":
        if company in taxi_companies_ranking:
            taxi_companies_ranking[company] += 1
        else:
            taxi_companies_ranking[company] = 1

records_without_taxi_company_info = 0
for company in taxi_dataset_companies:
    if company.capitalize() == "No value":
        records_without_taxi_company_info += 1

sorted_taxi_companies_ranking = dict(sorted(taxi_companies_ranking.items(), key=lambda item: item[1], reverse=True))
print(f"\nTaxi companies ranked by the highest number of ordered rides: {sorted_taxi_companies_ranking}")
print(f"\nThe number of records without information about the taxi company: {records_without_taxi_company_info}")


# 5. Time frame of the data
trips_start = taxi_dataset.display_column_data("trip_start_timestamp")
trips_start.sort()

# data format: 2014-04-01 00:00:00 UTC
date = [x[:10] for x in trips_start]

print(f"\nThe file contains information about taxi rides from the following time frame: {date[0]} - {date[(len(trips_start)) - 1]}")


# 6. The number of records with information about miles traveled.
# 7. The number of records with information about the duration of rides.
trip_miles = taxi_dataset.display_column_data("trip_miles")
trip_seconds = taxi_dataset.display_column_data("trip_seconds")

known_trip_miles = []
for value in trip_miles:
    if value.capitalize() != "No value":
        known_trip_miles.append(value)

known_trip_seconds = []
for value in trip_seconds:
    if value.capitalize() != "No value":
        known_trip_seconds.append(value)

print(f"\nThe number of records with information about miles traveled: {len(known_trip_miles)}")
print(f"\nThe number of records with information about the duration of rides: {len(known_trip_seconds)}")


# 8. The number of records with both information about miles traveled and the duration of the ride.
known_miles_and_seconds = 0

for miles, seconds in zip(trip_miles, trip_seconds):
    if miles.capitalize() != "No value" and seconds.capitalize() != "No value":
        known_miles_and_seconds += 1

print(f"\nThe number of records with both information about miles traveled and the duration of the ride: {known_miles_and_seconds}")


# 9. The frequency of occurrence of the dropoff community areas:
dropoff_community_area = taxi_dataset.display_column_data("dropoff_community_area")
dropoff_community_area_frequency = {}

for item in dropoff_community_area:
    if item in dropoff_community_area_frequency:
        dropoff_community_area_frequency[item] += 1
    else:
        dropoff_community_area_frequency[item] = 1

sorted_dropoff_area_frequency = dict(sorted(dropoff_community_area_frequency.items(), key=lambda item: item[1], reverse=True))
print(f"\nThe frequency of occurrence of the dropoff community areas: {sorted_dropoff_area_frequency}")


# 10. The most common payment method
payment_type = taxi_dataset.display_column_data("payment_type")
payment_types = {}

for item in payment_type:
    if item in payment_types:
        payment_types[item] += 1
    else:
        payment_types[item] = 1

sorted_payment_types = sorted(payment_types.items(), key=lambda x: x[1], reverse=True)

print("\nThe most common chosen payment method:")
for item, count in sorted_payment_types:
    print(f"{item}: {count}")


# 11. The number of registered trip tolls
tolls = []
for row in taxi_dataset.data:
    if row["tolls"] != "No value" and row["tolls"] != "0" and row["tolls"] != "":
        tolls.append(row)

trip_toll = 0
for row in tolls:
    trip_toll = trip_toll + 1

print(f"\nThe number of registered trip tolls: {trip_toll}")


# 12. Taxi companies with the highest number of tips
records_with_tips = []
for row in taxi_dataset.data:
    if row["tips"] not in ["No value", "0", ""]:
        records_with_tips.append(row)

tips_frequency = {}
for dictionary in records_with_tips:
    for key, value in dictionary.items():
        if key == "company" and value not in ["No value", "0", ""]:
            if value in tips_frequency:
                tips_frequency[value] += 1
            else:
                tips_frequency[value] = 1

sorted_tips_frequency = dict(sorted(tips_frequency.items(), key=lambda item: item[1], reverse=True))

print("\nTaxi companies with the highest number of tips:")
for company, frequency in sorted_tips_frequency.items():
    print(f"{company}: {frequency}")


# 13. The highest tips of taxi companies
tips = "tips"
highest_tips = {}
for dictionary in records_with_tips:
    for key, value in dictionary.items():
        if key == "company" and value not in ["No value", ""]:
            if value not in highest_tips or highest_tips[value] < dictionary[tips]:
                highest_tips[value] = dictionary[tips]

print(f"\nTaxi companies' highest tips:")
for company, tip in highest_tips.items():
    print(f"{company}: ${tip}")
