import pandas
drinks = pandas.read_csv("drinks.csv", usecols=["wine_servings", "country"])
wine = pandas.Series(drinks["wine_servings"].values, drinks["country"].values)
print(wine)
print(type(wine))