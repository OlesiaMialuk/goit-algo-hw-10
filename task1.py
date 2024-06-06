import pulp

model = pulp.LpProblem("Optimization Problem", pulp.LpMaximize)

lemonade = LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = LpVariable('Fruit Juice', lowBound=0, cat='Integer')

model += 3 * lemonade + 5 * fruit_juice, "Total Production"

model += 2 * lemonade + fruit_juice <= 100, "Water"
model += lemonade + 2 * fruit_juice <= 50, "Sugar"
model += lemonade + fruit_juice <= 30, "Lemon Juice"
model += 2 * fruit_juice <= 40, "Fruit Puree"

model.solve()

print("Status:", LpStatus[model.status])
print("Maximum Production:")
print("Lemonade:", value(lemonade))
print("Fruit Juice:", value(fruit_juice))
print("Total Production:", value(model.objective))