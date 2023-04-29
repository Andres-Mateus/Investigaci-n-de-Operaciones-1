# Importar la librería Pulp
import pulp as pl
# Crear un problema de minimización
prob = pl.LpProblem("Minimización de gastos", pl.LpMinimize)
# Crear las variables de decisión
x1 = pl.LpVariable("x1", lowBound=0)
x2 = pl.LpVariable("x2", lowBound=0)
x3 = pl.LpVariable("x3", lowBound=0)
# Agregar la función objetivo
prob += 180*x1 + 160*x2 + 120*x3, "Función objetivo"
# Agregar las restricciones
prob += 6*x1 + x2 + 2*x3 >= 46, "Restricción 1"
prob += 3*x1 + x2 + 3*x3 >= 26, "Restricción 2"
prob += 4*x1 + 6*x2 + x3 >= 30, "Restricción 3"
# Resolver el problema
prob.solve()
# Imprimir el estado del problema (1 = óptimo)
print("Estado:", pl.LpStatus[prob.status])
# Imprimir los valores de las variables de decisión
print("x1 =", pl.value(x1))
print("x2 =", pl.value(x2))
print("x3 =", pl.value(x3))
# Imprimir el valor de la función objetivo
print("Valor mínimo de la función objetivo =", pl.value(prob.objective))