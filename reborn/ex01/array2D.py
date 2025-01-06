family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

lines = len(family)
cols = len(family[0])

sFamily = family[1:3]

sLines = len(sFamily)
sCols = len(sFamily[0])
print(family)
print(f"My shape is : ({lines}, {cols})")
print(sFamily)
print(f"My new shape is : ({sLines}, {sCols})")
