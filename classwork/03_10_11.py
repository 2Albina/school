nums = []
k = 0
data = input()
for n in range(5):
    for i in data:
        k += 1
        if i == " ":
            break
    nums.append(int(data[:k]))
    data = data[k:]
    k = 0

S = nums[0]
N = nums[1]
K = nums[2]
A = nums[3]
B = nums[4]

N_s  = S/A
if N_s < N:
    S_i = S - N_s*A
    K_i = S_i/B
    if K_i > K:
        K_i = K
else:
    S_i = S - N*A
    K_i = S_i/B
    if K_i >= K:
        K_i = K
        S_o = S - (N*A + K_i*B)
        N_s = N + S_o/A
    else:
        S_o = S - (N*A + K_i*B)
        N_s = N + S_o/A

print(int(N_s), int(K_i))
