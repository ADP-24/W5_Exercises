movies = ['the crow' , 'scott pilgrim vs the world','shawn of the dead',
          'hot fuzz','saving private ryan','spirited away','inception','back to the future',
          'the dark knight','school of rock']

#print(f"The list 'movies' includes my top {len(movies)} favorite movies")

# print(movies)

print(sorted(movies))

movies.sort()
print(movies)

## The two list are exactly the same and in alphabetic order.

movies.append("Anchorman")

print(f"The list 'movies' now includes an my top {len(movies)} favoirte movies")

print(movies)