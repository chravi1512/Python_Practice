alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1={}
alien_1['name'] = 'Ravi'
alien_1['age'] = 21

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name in favorite_languages:
    language = favorite_languages[name].title()
    print(f"\n{name}'s favorite language is {language}")
##language = favorite_languages['sarah'].title()
##print(f"Sarah's favorite language is {language}.")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
print(favorite_languages)
print(favorite_languages.keys())
print("\n")
print(favorite_languages.values())

L = ['a','b', 'c']
print(L)
res = ''.join(L)
print(res)
print(type(res))

