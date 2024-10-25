li1 = {0,2,4,8,6}
li2 = {1,2,4,3,5}

union = li1 | li2
intersection = li1 & li2
difference = li1 - li2
symmetric_diff = li1^li2

print(f"Union of E and N is {union}")
print(f"Intersection of E and N is {intersection}")
print(f"ifference of E and N is {difference}")
print(f"Symmetric difference of E and N is{symmetric_diff}")
