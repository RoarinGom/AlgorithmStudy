# 1260원 거슬러 줘야할 때, 최소 동전 갯수 10,50,100,500
# 잔돈 money
money = 1260
# 잔돈 갯수 numOfCoins
numOfCoins = 0
for coin in [500, 100, 50, 10]:
    # 동전별 잔돈 갯수 n
    n = money // coin
    # 잔돈 갯수 계산
    numOfCoins += n
    # 잔돈 뺀 금액
    money -= (n*coin)
    print(f'{coin}원 동전 : {n}개')


print(f'잔돈의 최소 동전 갯수 값: {numOfCoins} 개')
