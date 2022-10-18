# Pyrhon3 code to demonstrate
# swap of key and value

# class KeyValueSwap:
kv_new1 = {'A': 1, 'B': 3, 'c': 5, 'D': 7, 'E': 13}
kv_new2 = {'P': 4, 'Q': 9, 'R': 16, 'S': 25, 'T': 36}

print(kv_new1)
print(kv_new2)

newdict = dict(map(reversed, kv_new1.items()))
newdict2 = dict(map(reversed, kv_new2.items()))
print(newdict)
print(newdict2)