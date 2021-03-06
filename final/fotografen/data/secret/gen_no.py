import sys
import random

# maxN - length
# ratio
# seed - random seed

inputs = sys.stdin.readline().strip().split()

N = int(inputs[0])
ratio = float(inputs[1])
seed = int(inputs[2])

rotations = ['U', 'H', 'N', 'V']
random.seed(seed)

# vary N a bit
if random.randrange(10) < 5:
    N -= random.randrange(N / 5)
k = max(1,int(ratio * N))

offsets = [0] * N
sweep = [0] * N

print N, k

for i in xrange(N-k+2):
    offsets[i] = random.randrange(4)
    if offsets[i] == 0:
        offsets[i] = 1

cur = 0
for i in xrange(N):
    cur += offsets[i]
    cur += sweep[i]
    if i + k < N:
        sweep[i+k] = 4-offsets[i]
    cur %= 4
    sys.stdout.write(rotations[cur])

print ""
