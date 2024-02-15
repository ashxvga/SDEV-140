"""
def my_function(fname = "Emil"):
    print("Hello", fname)

def main():
    my_function() #prints "Hello Emil"
    my_function("James") #changed the value of fname to "James" and prints Hello James

if __name__ == "__main__":
    main()

#2

def my_function(child1, child2, child3):
    print("The youngest child is:", child3)

def main():
    my_function(child1 = "Emil", child3 = "Pam", child2 = "Tom")

if __name__ == "__main__":
    main()
"""
def my_function(**child):
    print("The youngest child is:", child["fname"])

def main():
    my_function(fname = "Emil", fname2 = "Pam", fname3 = "Tom")

if __name__ == "__main__":
    main()