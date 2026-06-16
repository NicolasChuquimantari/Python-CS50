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
        date = input("Enter the date: ").strip()
        if "/" in date:
            date_format = date.split("/")
            month, day, year = date_format
            month, day, year = int(month),int(day), int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

        elif "," in date:
            date_format = date.split(",")
            month,day = date_format[0].split()
            day, year = int(day), int(date_format[1])
            month = month_list.index(month) + 1
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
    except ValueError:
        pass













