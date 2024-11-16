import pandas
drinks = pandas.read_csv("drinks.csv", usecols=["wine_servings", "country", "beer_servings", "spirit_servings"])
alcohols = pandas.DataFrame(drinks[["wine_servings", "beer_servings", "spirit_servings"]].values, drinks["country"].values)
sum_drinks = alcohols.sum(axis=1)
print(sum_drinks.sort_values())