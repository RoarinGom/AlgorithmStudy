# N 값일 때 -> 1 될 때까지 몇 번 연산해야하는가?
# : 조건(1.N에서 1을 빼거나, 2.N에서 K로 나눌 수 있다(나누어떨어질 경우만)
# (정당성 K값이 1보다 클 경우, 나누어 떨어질 경우에 나누기 부터 한다.

N = 25
K = 3
# N=int(input())
# K=int(input())
# N, K=map(int,input().split())
# 연산횟수 count
count = 0
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (N//K)*K
    count += (N-target)
    N = target
    if N < K:
        break
    count += 1
    N //= K

print(count)
