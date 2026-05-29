def convert(str):
    str_converted = str.replace(":)", "🙂") .replace(":(", "🙁")
    return str_converted

def main():
    str = input("Entry data: ")
    print(convert(str))

main()
