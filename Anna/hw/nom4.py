from math import ceil
s = "asdasda"
t = ""
for i in range(1, ceil(len(s)/2)+1):
      t = s[:i]
      if t == s[i:2*i] and s.count(t) == len(s)/len(t):
          print(s.count(t))
          break
else:
    print("No")
