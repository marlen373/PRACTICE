names = ["dex", "mes", "lo"]
scores = [85, 92, 78]

combined = list(zip(names, scores))
print(f"Zip result: {combined}")


print("Enumerate result:")
for index, name in enumerate(names, start=1):
    print(f"Index {index}: {name}")

#conversion & checking

val = int(scores[0])
print(val, type(val))
print(isinstance(val, int))
print(isinstance(names, list))