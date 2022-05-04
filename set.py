#los set no funcionan con indices y se usan llaves
colors = {"red", "blue", "black"}
print(type(colors))
#me fijo si un dato pertenece al set usando in
print("red" in colors)
colors.add("violeta")
print(colors)
#es util para datos que no necesitas ordenar
