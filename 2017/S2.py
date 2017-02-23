import sys, math

inp = sys.stdin.readlines()

nums = [int(i) for i in inp[1].split()]

nums.sort()

lows = nums[:math.ceil(len(nums)/2)]
lows.reverse()
highs = nums[math.ceil(len(nums)/2):]

out = []
for l in range(len(lows)):
	out.append(str(lows[l]))
	if l < len(highs):
		out.append(str(highs[l]))
print(" ".join(out))