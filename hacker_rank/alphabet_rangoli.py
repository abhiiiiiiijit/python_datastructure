def print_rangoli(size):
    # your code goes here
    width = 4 * size - 3#size+(size-1)+(size+(size-1)-1)
    height = 2 * size-1
    prefix_char = 96
    for i in range(1, height+1):
        if i <= height//2+1:
            center_piece = calculate_center(size, i, prefix_char)
        else: 
            rw = height%i + 1
            center_piece = calculate_center(size, rw, prefix_char)
        

        # # print(center_piece)
        # print(center_piece.center(width,'-'))
    

        # print(center_piece)
        print(center_piece.center(width,'-'))

def calculate_center(size, i, prefix_char):
    center_piece = ''
    for j in range(0,i,1):
        center_piece += chr(prefix_char + (size-j)) 
        if  j<i-1:
            center_piece +=  '-'
        
    center_piece += (center_piece[:-1][::-1])
    return center_piece
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)