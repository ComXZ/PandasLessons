import pandas
nutrition = pandas.read_csv("nutrition.csv")
nutrition.drop(columns=["Unnamed: 0"], inplace=True)
print(nutrition)
nutr_mini = nutrition.sample(n=10)
print(nutr_mini[["cholesterol", "total_fat"]])
vit_b12_loc = nutrition.columns.get_loc("vitamin_b12")
print(nutrition.iloc[:3,vit_b12_loc:])
print(nutr_mini.loc[:,"calories"].head(1))