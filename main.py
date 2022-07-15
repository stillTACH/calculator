from functools import reduce


def add(*numbers):
    return sum(*numbers)

def diff(number1,number2):
    return number1 - number2

def product(*numbers):
    def mult(x,y):
        return x*y
    return reduce(mult,*numbers)

def divide(number1,number2):
    return number1 / number2





if __name__ == '__main__':
    while True:
        try:
            print("""
            1. add
            2. diff
            3. product
            4. divide
            5. exit
            """)
            user_in = input("Enter your selection:")
            if user_in == "5":
                break

            numbers = []
            while True:
                try:
                    num1 = int(input("Enter number:"))
                    numbers.append(num1)
                except Exception as e:
                    break


            if user_in == "1":

                print(add(numbers))

            if user_in == "2":

                print(diff(number1,number2))

            if user_in == "3":

                print(product(numbers))

            if user_in == "4":

                print(divide(number1, number2))
        except Exception as e:
            print(f"An exception happened, start over\nERROR: {e}")



    # thesum = add(5, 2)
    # print(thesum)
    # thesum = add(8, 4)
    # print(thesum)
    # thediff = diff(3,5)
    # print(thediff)
    # print(add(4, diff(3, 8)))
