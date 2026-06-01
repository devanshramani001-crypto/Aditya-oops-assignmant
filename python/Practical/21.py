# Write a Python program to count how many times each
# character appears in a string
text="banana"
freq={}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
print(freq)