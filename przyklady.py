os = {
    'imie':'sławek',
    'nazwisko':'Bo',
    'nr_k':1,
    'stan':100
}
lst = [os, {
    'imie':'Gosia',
    'nazwisko':'Samosia',
    'nr_k':3,
    'stan':10000
}]

for item in lst:
    if item['nr_k'] == 3:
        item['stan'] += 1000

print(lst)