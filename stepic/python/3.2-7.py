s = input()
t = input()

results = 0
sub_len = len(t)
for i in range(len(s)):
    if s[i:i+sub_len] == t:
        results += 1

print(results)
