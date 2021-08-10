import re

m = {}
with open("words") as file:
    for line in file:
        splitted = re.split(r'_+', line.strip().lower())
        for w in splitted:
            m[w] = m.get(w, 0) + 1

for k,v in m.items():
    print("{}:{}".format(k, v))

print("total!!!: ", sum(m.values()))