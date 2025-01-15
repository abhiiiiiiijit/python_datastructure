
from  cmath import  phase

def print_r_phi(complex_no):
    print(abs(complex_no))
    print(phase(complex_no))

if __name__ == "__main__":
    complex_no = input("Enter complex number: ")
    ####doesn't work when only real or imaginery input
    # x, y = complex_no.split('+')
    # x = int(x)
    # y = int(y[:-1])
    #######################
    complex_no = complex(complex_no)
    print_r_phi(complex_no)
