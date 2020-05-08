countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

ind_ger = countries.index('germany')
capitals[ind_ger]

europe = { 'spain': 'madrid',
           'france': 'paris',
           'germany': 'berlin',
           'norway': 'oslo' }

print(europe)
print(europe.keys())
print(europe['norway'])

europe['italy'] = 'rome'
print('italy' in europe)

europe['poland'] = 'warsaw'
print(europe)

europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

europe['germany'] = 'berlin'
del(europe['australia'])

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

print(europe['france']['capital'])

data = { 'capital': 'rome',
         'population': 59.83 }

europe['italy'] = data

print(europe)