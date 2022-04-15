pet_1 = {'name':'cat','owner':'rtq'}
pet_2 = {'name':'dog','owner':'lxb'}
pet_3 = {'name':'rabbit','owner':'wc'}
pets = [pet_1,pet_2,pet_3]
for pet in pets:
    print(pet)
print('\n\n')


favourite_places = {
    'rtq':['Paris','Shanghai'],
    'lxb':['Xian','Dalian'],
    'mlc':['Beijing'],
    }
for name,places in favourite_places.items():
    if len(places) == 1:
        print(name.title()+"'s favourite place is "+places[0]+'.')
    else:
        print(name.title()+"'s favourite places are:")
        for place in places:
            print(place)
print('\n\n')


cities = {
    'Beijing':{'country':'China','population':'large','fact':'capital'},
    'Shanghai':{'country':'China','population':'large','fact':'magic city'},
    'Paris':{'country':'France','population':'medium','fact':'beautiful'},
    }
for city,features in cities.items():
    print('city name:'+city)
    print('country:'+features['country'])
    print('population:'+features['population'])
    print('fact:'+features['fact'])
    print('\n')
