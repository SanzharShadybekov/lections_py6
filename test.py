import random 

ls = {'Watch Toples on Youtube': 0, 'Read the book': 0, 'Scroll Instagram': 0}
rounds = 1_000_000 
i = 1

while i < rounds:
    chislo = random.randint(1, 3) # 1,2,3
    if chislo == 1:
        ls['Watch Toples on Youtube'] += 1
    elif chislo == 2:
        ls['Read the book'] += 1
    else:
        ls['Scroll Instagram'] += 1
    print(i)
    i = i + 1

print(ls)
