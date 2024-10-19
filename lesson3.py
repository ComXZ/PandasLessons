import pandas
drinks = pandas.read_csv("drinks.csv", usecols=["wine_servings", "country"], index_col="country", squeeze=True)
wine = pandas.Series(drinks["wine_servings"].values, index = drinks["country"].values)
print(drinks)
print(type(wine))