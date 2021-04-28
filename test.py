import pyupbit

access = "8dpB37J8nmQ61UxNGoPtXubwcU3m8rxNXQVWiHTl"          # 본인 값으로 변경
secret = "RjjIRCFromwpw2IkcA9P1xHTgMQlwsZ0TfAFNxZO"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
