import pandas

# actor_names = ["Johny Depp", "Leonardo Dicaprio", "Will Smith", "Elizabeth Olsen"]
# actor_ages = [45, 56, 61, 37]

# actors = pandas.Series(actor_ages, actor_names)
# print(actors)

actor_names = ["Johny Depp", "Leonardo Dicaprio", "Will Smith", "Elizabeth Olsen"]
actor_ages = [45, 56, 61, 37]

actor_dict = {"Johny Depp" : 45, "Leonardo Dicaprio" : 56, "Will Smith" : 61, "Elizabeth Olsen" : 37}
actors = pandas.Series(actor_dict)

print(actors)