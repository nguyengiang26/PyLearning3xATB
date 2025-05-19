hero1 = ("Batman", "Bruce Wayne", "Gotham City")
hero2 = ("Superman", "Clark Kent", "Metropolis")

new_hero = hero1 + hero2
print(new_hero) # Output: ('Batman', 'Bruce Wayne', 'Gotham City', 'Superman', 'Clark Kent', 'Metropolis')

new_hero = hero1 * 2
print(new_hero) # Output: ('Batman', 'Bruce Wayne', 'Gotham City', 'Batman', 'Bruce Wayne', 'Gotham City')

new_hero = (hero1, hero2)
print(new_hero) # Output: (('Batman', 'Bruce Wayne', 'Gotham City'), ('Superman', 'Clark Kent', 'Metropolis'))
print(new_hero[0]) # Output: ('Batman', 'Bruce Wayne', 'Gotham City')
print(new_hero[0][0]) # Output: 'Batman'
print(new_hero[1][0]) # Output: 'Superman'