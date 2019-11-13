import random
fortune = random.sample(range(0, 51), 15)
print(fortune)
screening_out = [el for num, el in enumerate(fortune) if fortune[num] > fortune[num - 1]]
print(screening_out[1:])


