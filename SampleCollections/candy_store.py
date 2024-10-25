candies = ('skittles','starburst','trolli')

fruity_flavors = ('blueberry blast', 'kiwi lime', 'dragonfruit delight')

candy_combinations = set()

candy_combinations.add((candies[0], fruity_flavors[2]))
candy_combinations.add((candies[1], fruity_flavors[0]))
candy_combinations.add((candies[2], fruity_flavors[1]))

output_message = f"Today's candy options include: {candy_combinations}"

print(output_message)

#5 The order of the items change everytime the above print statment is run.