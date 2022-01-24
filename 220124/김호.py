#없는 숫자 더하기

def solution(numbers):
    row = list(range(0, 10))
    not_in = []

    for num in row:
        if num in numbers:
            continue
        else:
            not_in.append(num)

    return sum(not_in)


print(solution([1,2,4,5,8,9]))
