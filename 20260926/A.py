c = input()

light = ["B", "Y", "R"]

for k, v in enumerate(light):
    if v == c:
        print(light[(k+1)%3])
