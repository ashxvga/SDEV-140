def ageIn5(x):
    result = x+5
    print("Your age in 5 years will be", result)

def fNameFuction(fName):
    print("Hello", fName)

def main():
    firstName = input("Enter your first name: ")
    fNameFuction(firstName)
    age = int(input("Enter your age: "))
    ageIn5(age)


if __name__ == "__main__":
    main()