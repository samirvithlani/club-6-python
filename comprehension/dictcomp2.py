countries = ["India", "USA", "UK", "China", "Russia","France"]
capital =["New Delhi", "Washington", "London", "Beijing", "Moscow"]

data ={}

#india

# for i in range(len(countries)):
#     data[countries[i]] = capital[i]
    
# for (i,j) in zip(countries,capital):
#     data[i] = j

data = {i:j for (i,j) in zip(capital,countries)}        
print(data)