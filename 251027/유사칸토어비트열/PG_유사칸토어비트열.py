def solution(n, l, r):
    answer = 0

    for i in range(l-1,r):
        while i>0:
            # i % 5 == 2 인 위치에 있는 경우,
            # 0이 해당 위치에 존재함. 
            # (계속해서 5개의 섹션으로 나누며, 가운데 즉, 2번 인덱스 위치에 있는지 확인 ) 
            if i % 5 != 2:
                i//=5 
            else: 
                break
        
        #1인 경우
        if i == 0:
            answer +=1

    return answer