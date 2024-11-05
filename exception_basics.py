
def divide_numbers(n_tcases: int)-> None:
    for _ in range(n_tcases):
        try:
            x, y = map(int, input().split(" "))
            print(x//y)
        except ZeroDivisionError as zde:
            print(f"Error Code: {zde}")
        except ValueError as ve:
            print(f"Error Code: {ve}")


if __name__ == "__main__":
    n_tcases = int(input("Enter no of test cases:"))
    divide_numbers(n_tcases)