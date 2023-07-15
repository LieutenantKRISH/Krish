def is_leap_year(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False

        else:
            return True
    else:
        return False

if __name__ == "__main__":
    n = int(input("enter your year"))
    print(is_leap_year(n))

