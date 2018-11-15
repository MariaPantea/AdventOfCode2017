import math

n = 26


#levels = [1^2, 3^2, 5^2, 7^2, 9^2, 11^2...] 

# 1
# 2-3^2
# 10-5^2
# 26-7^2
# 50-9^2

level = range(1,int(math.sqrt(n)),2)

print level


