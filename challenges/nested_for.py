if __name__ == '__main__':
    stu_mrk = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu_mrk.append([name,score])
        
    stu_mrk.sort(key=lambda x:x[1])
    lowest_2 = []
    change = 0
    for i in range(1,len(stu_mrk)):
        if stu_mrk[i][1] != stu_mrk[0][1] and change == 0:
            change = 1
            lowest_2.append(stu_mrk[i])
        elif change == 1:
            if lowest_2[0][1]== stu_mrk[i][1]:
                lowest_2.append(stu_mrk[i])
            else:
                break
    lowest_2.sort(key= lambda x:x[0])
    for e in lowest_2:
        print(e[0])
    
    
