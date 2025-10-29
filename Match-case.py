#Alternative way of elif

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

def main():
    print(is_weekend("Monday"))


if __name__ == '__main__':
    main()