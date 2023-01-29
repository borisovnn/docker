i = 0
fn = 0
sn = 0

print("Hello, please choose the action: 1-4", '\n', "1) +", '\n', "2) -", '\n', "3) *", '\n', "4) /", '\n', "Action: ")
i = int(input())

print("first number is: ")
fn = int(input())

print("second number is: ")
sn = int(input())

if i == 1: print("Result: ", fn + sn)
if i == 2: print("Result: ", fn - sn)
if i == 3: print("Result: ", fn * sn)
if i == 4: print("Result: ", fn / sn)