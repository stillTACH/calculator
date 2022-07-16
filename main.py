from functools import reduce


def add(*numbers):
    x = sum(*numbers)
    return x

def diff(*numbers):
    sub1 = numbers[0][0]
    for num1 in numbers[0][1:]:
        sub1 -= num1
    return sub1

def product(*numbers):
    def mult(x,y):
        return x*y
    return reduce(mult,*numbers)

def divide(*numbers):
    sub1 = numbers[0][0]
    for num1 in numbers[0][1:]:
        sub1 /= num1
    return sub1




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
# make input validation work here..

            if user_in == "1":
                results = add(numbers)
                print(results)
            if user_in == "2":
                print(diff(numbers))
            if user_in == "3":
                print(product(numbers))
            if user_in == "4":
                print(divide(numbers))

        except Exception as e:
            print(f"An exception happened, start over\nERROR: {e}")


