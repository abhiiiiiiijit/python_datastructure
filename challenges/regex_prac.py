if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        cmnd = input().split()
        if (cmnd[0] == 'insert'):
            ind = int(cmnd[1])
            e = int(cmnd[2])
            lst.insert(ind,e)
        elif (cmnd[0] == 'print'):
            print(lst)
        elif (cmnd[0] == 'remove'):
            e = int(cmnd[1])
            lst.remove(e)
        elif (cmnd[0] == 'append'):
            e = int(cmnd[1])
            lst.append(e)
        elif (cmnd[0] == 'sort'):
            lst.sort()
        elif (cmnd[0] == 'pop'):
            lst.pop()
        elif (cmnd[0] == 'reverse'):
            lst.reverse()
