if __name__ == '__main__':
    new_score_list=[]
    final_list=[]
    name_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        new_score_list.append(score)
        final_list.append([name,score])
    s=list(set(new_score_list))
    s.sort()
    sl=s[1]
    for name,score in final_list:
        if(score==sl):
            name_list.append(name)
    
    name_list.sort()
    for i in name_list:
        print(i)        
