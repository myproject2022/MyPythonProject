# sample and simple question of dictionary in python
test_string = 'occurrence'

all_string = {}

for i in test_string:
    if i in all_string:
        all_string[i] += 1
    else:
        all_string[i] = 1

print("key and value of test character :", str(all_string))
