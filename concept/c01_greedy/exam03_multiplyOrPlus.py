given_val = "02984"

nums = list(map(int, given_val))
# 가장 큰 값 구하기 answer
answer = 0
for i in range(len(nums)):
    num = nums[i]
    if answer == 0:
        answer += num
    else:
        if num == 1 or num == 0:
            answer += num
        else:
            answer *= num
print(answer)
