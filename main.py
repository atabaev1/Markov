
import numpy as np


state = {
    0 : "BMW",
    1 : "Toyota",
    2 : "Lexus"
}
state
A = np.array([[0.2, 0.6, 0.2], [0.3, 0.0, 0.7], [0.5, 0.0, 0.5]])


#Random Walk
n = 15
start_state = 0
curr_state = start_state
print(state[curr_state], "--->", end=" ")


while n-1:
    curr_state = np.random.choice([0, 1, 2], p=A[curr_state])
    print(state[curr_state], "--->", end=" ")
    n-=1
print("stop")

#Monte Carlo
steps = 10**6
start_state = 0
curr_state = start_state
pi = np.array([0, 0, 0])
pi[start_state] = 1

i = 0
while i<steps:
    curr_state = np.random.choice([0,1,2], p=A[curr_state])
    pi[curr_state]+=1
    i +=1

print("π = ", pi/steps)

#Repead Matrix
steps = 10**3
A_n = A

i=0
while i<steps:
    A_n =  np.matmul(A_n, A)
    i+=1

print("A^n = \n", A_n, "\n")
print("π = ", A_n[0])

#Finding Left Eigen Vectors
import scipy.linalg
values, left = scipy.linalg.eig(A, right = False, left = True)

print("left eigen vectors = \n", left, "\n")
print("eigen values = \n", values)

pi = left[:,0]
pi_normalized = [(x/np.sum(pi)).real for x in pi]
pi_normalized


#P(Pizza --> Hotdog --> Hotdog --> Burger) = ?
def find_prob(seq, A, pi):
    start_state = seq[0]
    prob = pi[start_state]
    prev_state, curr_state = start_state, start_state
    for i in range(1, len(seq)):
        curr_state = seq[i]
        prob *= A[prev_state][curr_state]
        prev_state = curr_state
    return prob

print(find_prob([1, 2, 2, 0], A, pi_normalized))