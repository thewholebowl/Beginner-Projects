values = {"i": 1,"v": 5,"x": 10,"l": 50,"c": 100,"d": 500,"m": 1000}
s = 0
x = input("Enter Roman numeral: ").strip().lower()
i = 0
while i < len(x):
    if i + 1 < len(x) and values[x[i]] < values[x[i + 1]]:
        s += values[x[i + 1]] - values[x[i]]
        i += 2
    else:
        s += values[x[i]]
        i += 1
print(s)
