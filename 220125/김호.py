#핸드폰 번호 가리기
def solution(phone_number):
    num_list = list(str(phone_number))
    star = '*' * (len(phone_number) - 4)
    num_list[0:-4] = star
    answer = "".join(num_list)
    return answer
