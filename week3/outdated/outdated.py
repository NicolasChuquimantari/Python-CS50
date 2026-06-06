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
            month, day, year = date_format



