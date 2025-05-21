import sys
import itertools

def apply_ops(a,b, op):
    if op=="+":
        return a + b
    if op=="-":
        return a-b
    if op=="*":
        return a*b
    
def ablity_to_make_forty_two(numbers):
    operators=['+','-','*']

    for num_perms in itertools.permutations(numbers):
        for ops in itertools.product(operators, repeat=4):
            result=apply_ops(num_perms[0],num_perms[1], ops[0] )
            result=apply_ops(result,num_perms[2], ops[1] )
            result=apply_ops(result,num_perms[3], ops[2] )
            result=apply_ops(result,num_perms[4], ops[3] )

            if result==42:
                print(num_perms[0], ops[0],num_perms[1], ops[1],num_perms[2], ops[2],num_perms[3], ops[3],num_perms[4])
                return True
            
    else:
        return False
    

for line in sys.stdin:
    numbers = list(map(int, line.strip().split()))

    print("YES" if ablity_to_make_forty_two(numbers) else "NO")