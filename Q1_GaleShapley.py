# O(n^2)
def stable_match(men_prefs, women_prefs):

    free_men = list(men_prefs.keys())
    engagements = {}
    
    while free_men:
        man = free_men.pop(0)
        
        man_pref = men_prefs[man]
        
        woman = man_pref.pop(0)
        fiance = engagements.get(woman)
        
        if not fiance:
            engagements[woman] = man
        else:
            if women_prefs[woman].index(man) < women_prefs[woman].index(fiance):
                engagements[woman] = man
                free_men.append(fiance)
            else:
                free_men.append(man)
    return engagements


men_prefs = {}
women_prefs = {}

num = int(input("enter no. of mens/womens: "))

print("Enter mens preference")
for i in range(num):
    ans = input(f"Enter the man {i+1} followed by his preferences: ").split()
    men_prefs[ans[0]] = ans[1:]

for i in range(num):
    ans  = input(f"Enter the woman {i+1} followed by her preferences: ").split()
    women_prefs[ans[0]] = ans[1:]

stableMatches = stable_match(men_prefs, women_prefs)
print("Stable Marriages:")
for woman, man in stableMatches.items():
    print(f"{man} is engaged to {woman}")


# men_prefs = {
#     'm1': ['w1', 'w2', 'w3'],
#     'm2': ['w2', 'w3', 'w1'],
#     'm3': ['w2', 'w1', 'w3']
# }

# women_prefs = {
#     'w1': ['m2', 'm3', 'm1'],
#     'w2': ['m1', 'm2', 'm3'],
#     'w3': ['m1', 'm3', 'm2']
# }