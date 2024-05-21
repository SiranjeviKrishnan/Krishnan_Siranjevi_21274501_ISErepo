import datetime

def lpn(dob):
    dstr = dob.strftime('%Y%m%d')
    num = sum(int(d) for d in dstr)
    while num > 9 and num not in [11, 22, 33]:
        num = sum(int(d) for d in str(num))
    return num

def is_master(n):
    return n in [11, 22, 33]

def lucky_color(n):
    colors = {
        1: "Red", 2: "Orange", 3: "Yellow", 4: "Green", 5: "Blue",
        6: "Indigo", 7: "Violet", 8: "Purple", 9: "Gold",
        11: "Silver", 22: "Platinum", 33: "Diamond"
    }
    return colors.get(n, "Unknown")

def compare_lpn(dob1, dob2):
    return lpn(dob1) == lpn(dob2)

def get_gen(dob):
    year = dob.year
    gens = [
        (1901, 1927, "Greatest Generation"),
        (1928, 1945, "Silent Generation"),
        (1946, 1964, "Baby Boomers"),
        (1965, 1980, "Generation X"),
        (1981, 1996, "Millennials"),
        (1997, 2012, "Generation Z"),
        (2013, 2024, "Generation Alpha")
    ]
    return next((gen for start, end, gen in gens if start <= year <= end), "Unknown Generation")

def main():
    while True:
        print("""
            !!! Welcome to the Program !!!
                    
            1. Calculate Life Path Number
            2. Check if a number is a master number
            3. Get the lucky color based on Life Path Number
            4. Compare Life Path Numbers of two birthdays
            5. Determine the generation of a person
            0. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            dob = datetime.datetime.strptime(input("Enter your birthday (YYYY-MM-DD): "), "%Y-%m-%d")
            print(f"Your Life Path Number is: {lpn(dob)}")
        elif choice == "2":
            num = int(input("Enter a number: "))
            print(f"{num} is a master number: {is_master(num)}")
        elif choice == "3":
            n = int(input("Enter your Life Path Number: "))
            print(f"Your lucky color is: {lucky_color(n)}")
        elif choice == "4":
            dob1 = datetime.datetime.strptime(input("Enter the first birthday (YYYY-MM-DD): "), "%Y-%m-%d")
            dob2 = datetime.datetime.strptime(input("Enter the second birthday (YYYY-MM-DD): "), "%Y-%m-%d")
            print(f"Life Path Numbers are the same: {compare_lpn(dob1, dob2)}")
        elif choice == "5":
            dob = datetime.datetime.strptime(input("Enter your birthday (YYYY-MM-DD): "), "%Y-%m-%d")
            print(f"You belong to the {get_gen(dob)}")
        elif choice == "0":
            exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()