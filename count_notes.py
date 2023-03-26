count = 0
with open("test_freq.txt") as f:
    notes = f.read().split(" ")
    for note in notes:
        count += 1

print(count)