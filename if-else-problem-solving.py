# Problem:  
# Source: HackerRank.com

'''Task
Given an integer,N , perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of 2 to 5, print Not Weird
If N  is even and in the inclusive range of 6 to 20, print Weird
If N is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, n.

Constraints
1<= 0 <= 100

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.'''

# Start Solving this problem

n = int(input().strip())

if n%2 == 0 and n in range(2,6):
    print("Not Weird")
elif n%2 == 0 and n in range(6,21):
    print("Weird")
elif n%2 == 0 and n > 20:
    print("Not Weird")
else:
    print("Weird")