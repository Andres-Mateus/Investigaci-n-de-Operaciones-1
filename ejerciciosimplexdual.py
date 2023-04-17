import pulp
# importar el paquete pulp, que es una librería de Python para
# resolver problemas de programación lineal
prob = pulp.LpProblem("Minimización de costo", pulp.LpMinimize)

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
y1 = pulp.LpVariable("y1", lowBound=0)
y2 = pulp.LpVariable("y2", lowBound=0)
y3 = pulp.LpVariable("y3", lowBound=0)

prob += 6*y1 + 3*y2 + 4*y3 >= 180
prob += y1 + y2 + 6*y3 >= 160
prob += 12*y1 + 8*y2 + 24*y3 == 1*x1 + 0*x2
 
status = prob.solve()
print("Estado de la solución:", pulp.LpStatus[status])
print("Valor óptimo de Z:", pulp.value(prob.objective))
print("Solución óptima:")
print("x1 =", pulp.value(x1))
print("x2 =", pulp.value(x2))
print("y1 =", pulp.value(y1))
print("y2 =", pulp.value(y2))
print("y3 =", pulp.value(y3))
