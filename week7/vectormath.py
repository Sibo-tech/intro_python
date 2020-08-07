vec_a = list(map(int, input("Enter vector A:\n").split()))
vec_b = list(map(int, input("Enter vector B:\n").split()))
vec_add = []
vec_dot = []
vec_nom_a = []
vec_nom_b = []
import math
for i in range(0, len(vec_a)):
    vec_add.append(vec_a[i] + vec_b[i])
    vec_dot.append(vec_a[i] * vec_b[i])
    vec_dot_sum = sum(vec_dot)
    vec_nom_a.append(pow(vec_a[i], 2))
    vec_nom_a_sum = math.sqrt(sum(vec_nom_a))
    vec_nom_b.append(pow(vec_b[i], 2))
    vec_nom_b_sum = math.sqrt(sum(vec_nom_b))

print("A+B = " + str(vec_add))
print("A.B = " + str(vec_dot_sum))
print("|A| = " + str(round(vec_nom_a_sum,2)))
print("|B| = " + str(round(vec_nom_b_sum,2)))