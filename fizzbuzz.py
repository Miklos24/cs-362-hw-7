def fizzbuzz():
    arr = list(range(1, 101))
    for i in range(100):
        if arr[i] % 3 == 0:
            if arr[i] % 5 == 0:
                arr[i] = 'FizzBuzz'
            else:
                arr[i] = 'Fizz'
        elif arr[i] % 5 == 0:
            arr[i] = 'Buzz'
    return arr
            


if __name__ == '__main__':
    print(fizzbuzz())