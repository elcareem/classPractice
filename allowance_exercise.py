allowance = 2000
print(f"My allowance is N{allowance}")

allowance -= 400
print(f"I've spent N400 on books, my balance is N{allowance}")

allowance += 100
print(f"I've found N100 under my bed, my balance is N{allowance}")

allowance -= 250
print(f"I've spent N250 on snacks, my balance is N{allowance}")

allowance -= allowance * (25/100)
print(f"I've spent 25% of my current allowance on my siblings, my balance is N{allowance}")

allowance -= allowance * (1/3)
print(f"I've spent one-third of what's left to buy data, my balance is N{allowance}")

half_allowance = allowance // 2
savings = half_allowance
tithing = half_allowance

print(f"I've split my remaining allowance of N{allowance} equally, my savings is now N{savings} and tithe is N{tithing}")

savings %=  100
print(f"The remaining balance after removing all N100 notes is {savings}")

