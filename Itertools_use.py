from itertools import product, permutations

########################### product use ########################
# a = input().split(' ')
# b = input().split(' ')

# a = [int(e) for e in a]
# b = [int(e) for e in b]

# cart_prod = list(product(a,b))

# print(*cart_prod)
# for e in cart_prod:
#     print(e, end ='')
################################################ permutation ###


def generate_permutations(string_input, combination_length):
    """Generate all permutations of a string with a specified length.

    Args:
        string_input (str): The input string to permute.
        combination_length (int): Length of each permutation.

    Returns:
        None
    """
    print(string_input)
    string_input = sorted(string_input) 
    print(string_input) # Sort input for lexicographical order
    for combination in permutations(string_input, combination_length):
        print(''.join(combination))

if __name__ == "__main__":
    try:
        # Take input and convert to appropriate data types
        string_input, combination_length = input("Enter a string and an integer: ").split()
        combination_length = int(combination_length)
        generate_permutations(string_input, combination_length)
    except ValueError:
        print("Invalid input. Please enter a string followed by an integer.")

##############################################################