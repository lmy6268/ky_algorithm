#https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    sn = set(nums)
    answer = min(len(sn),len(nums)//2)
    
    return answer