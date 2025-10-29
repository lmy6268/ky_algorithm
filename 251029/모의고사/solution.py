def solution(answers):
    answer = []
    
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0,0,0]
    
    #원형 리스트로 생각하고, 탐색 
    for i,v in enumerate(answers):
        if n1[i%5] == v:
            scores[0] +=1
        if n2[i%8] == v:
            scores[1] +=1
        if n3[i%10] == v:
            scores[2] +=1
    
    ms = max(scores)
    for i,v in enumerate(scores):
        if v == ms:
            answer.append(i+1)
    
    
    
    return answer