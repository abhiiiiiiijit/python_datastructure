if __name__ == '__main__':
    s = input()
    print(True if bool([c for c in s if c.isalnum()]) else False)
    print(True if bool([c for c in s if c.isalpha()]) else False)
    print(True if bool([c for c in s if c.isdigit()]) else False)
    print(True if bool([c for c in s if c.islower()]) else False)
    print(True if bool([c for c in s if c.isupper()]) else False)
