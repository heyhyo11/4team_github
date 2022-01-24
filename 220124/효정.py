# 프로그래머스

# 문제 1.코딩테스트 연습 > 월간코드챌린지 시즌3 > 없는 숫자 더하기
# https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3

def solution(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    answer = 45 - sum
    return answer

# 다른 사람들의 풀이
def solution(numbers):
    return 45 - sum(numbers)





# 문제 2.코딩테스트 연습 > 연습문제 > 평균 구하기
# https://programmers.co.kr/learn/courses/30/lessons/12944?language=python3

def solution(arr):
    return sum(arr)/len(arr)