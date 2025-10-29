def solution(sizes):

    # 원래 코드 
    # answer = 0
    #     newSizes = []
    #     wallet = [0,0]
    #     for w,h in sizes:
    #         if w>=h:
    #             newSizes.append((w,h))
    #         else:
    #             newSizes.append((h,w))
            
    #         wallet[0] = max(wallet[0],newSizes[-1][0])
    #         wallet[1] = max(wallet[1],newSizes[-1][1])
                    
    #     answer = wallet[0] * wallet[1]

    #조금 최적화한 코드 -> 굳이 리스트에 담을 필요가 없음. 
    r = 0
    c = 0 
    for w,h in sizes: 
        if w < h : 
            w,h = h,w
        r = max(w,r)
        c = max(h,c)
    
    return r*c