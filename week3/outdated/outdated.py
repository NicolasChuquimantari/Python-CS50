month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Enter the date: ")
        if "/" in date:
            date_format = date.split("/")
            month, day, year = int(date_format)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
        else:
            





