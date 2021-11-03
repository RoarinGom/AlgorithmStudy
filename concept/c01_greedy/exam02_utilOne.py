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
while N != 1:
    count += 1
    if K < 2:
        N -= 1
    else:
        if N % K == 0:
            N //= K
        else:
            N -= 1
print(f'최소 연산 횟수 : {count}')
