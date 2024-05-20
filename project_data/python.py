# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding 
# 1. storing the best math schools in a pandas Datafram, only storing schools with an average math score of above 640
best_math_schools = schools[schools["average_math"] / 800 >= 0.8][["school_name", "average_math"]].sort_values("average_math", ascending=False)

#print(best_math_schools)
# 2. Indentifying the top 10 schools by finding the mean of the column total_SAT and sorting these values in descending order
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools.groupby("school_name")["total_SAT"].mean().reset_index().sort_values("total_SAT", ascending=False).head(10)
#print(top_10_schools)

# 3. Now creatng the pandas dataframe largest_std_dev, and locating the NYC Borough with the largest variation
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

# 4. Adding the count, mean and the standard deviation to largest_std_dev
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

print(largest_std_dev)
