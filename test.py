import pyupbit

access = "xSWZamGD2jMwXBynfSOCnGxKKFxCS9Xz3GXJevHH"          # 본인 값으로 변경
secret = "4xhoITi6BsxujWlkzxCMELujgBREjT3boib30R0w"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
