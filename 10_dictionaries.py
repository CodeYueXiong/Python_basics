# Defining a dictionary
webstersDict = {'person': 'a human being, whether an adult or child',
                'marathon': 'a running race that is about 26 miles',
                'resist': ' to remain strong against the force or effect of (something)',
                'run': 'to move with haste; act quickly'}
print(webstersDict)
# Accessing values in a Dictionary, using dictionary[key]
var = webstersDict['marathon']
print(var)
# Updating Dictionary
webstersDict['shoe'] = 'an external covering for the human foot'
print(webstersDict['shoe'])
# or using the `update` method, add more key-element to the original dictionary
webstersDict.update({'shirt': 'a long- or short-sleeved garment for the upper part of the body',
                     'shoe': 'an external covering for the human foot, usually of leather and consisting of a more or '
                             'less stiff or heavy sole and a lighter upper part ending a short distance above, at, '
                             'or below the ankle.'})
print(webstersDict)
# Removing keys from Dictionary
del webstersDict['resist']
print(webstersDict.keys())
# Returning values using the `get()`
storyCount = {'is': 100,
              'the': 90,
              'Michael': 12,
              'runs': 5}
print(storyCount.get('Michael'))
# Iterating through Dictionaries
# returns keys in a dict
print(storyCount.keys())
# returns values in a dict
print(storyCount.values())
# using for loop
for key in storyCount:
    print(key)
for key, value in webstersDict.items():
    print(key, value)