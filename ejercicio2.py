import pulp

# Crear problema de programación lineal
prob = pulp.LpProblem("Coste minimo de produccion", pulp.LpMinimize)

# Definir variables de decisión
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)

# Definir función objetivo
prob += 4*x1 + 12*x2 + 18*x3

# Definir restricciones
prob += x1 + 3*x3 >= 3
prob += 2*x2 + 2*x3 >= 5

# Resolver problema
prob.solve()

# Imprimir resultados
print("Status: ", pulp.LpStatus[prob.status])
print("Valor óptimo de x1 = ", pulp.value(x1))
print("Valor óptimo de x2 = ", pulp.value(x2))
print("Valor óptimo de x3 = ", pulp.value(x3))
print("Valor óptimo de la función objetivo = ", pulp.value(prob.objective))