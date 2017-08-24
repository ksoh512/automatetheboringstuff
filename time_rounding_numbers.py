import time

now = time.time()
print(now)

now_round_to_hundredth = round(now, 2)
print(now_round_to_hundredth)

now_round_to_ten_thousandth = round(now, 4)
print(now_round_to_ten_thousandth)

now_round_to_whole_number = round(now)
print(now_round_to_whole_number)
