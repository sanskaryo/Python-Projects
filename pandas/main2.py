import pandas as pd

data = pd.read_csv(r"D:\sankhu codes and stuff\angela yu course\python\pandas\weather_data.csv")

print(data["temp"])

temperatures = data['temp'].tolist()

print(temperatures)

print()

monday = data[data.day == "Monday"]
print(monday.condition)


data_dict = {
    
    "students" : ["sankho", "john doe", "guruji"],
    
    "scores" : [76,56,65]    
    
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
