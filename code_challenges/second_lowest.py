if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
    
    l.sort(key=lambda x: (x[1], x[0]))
    
    lowest = l[0][1]
    second_lowest = None
    
    for name, score in l:
        if score != lowest:
            second_lowest = score
            break
    
    for name, score in l:
        if score == second_lowest:
            print(name)
        
