# 10 minutes to pandas
import pandas as pd
import numpy as np 
# pandas provides two types of classes for handling data:

# 1. Series: a one-dimensional labeled array holding data of any type
# such as integers, strings, Python objects etc.

# 2. DataFrame: a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.
s = pd.Series([1,3,5 , np.nan, 6,8])
print(s)

dates = pd.date_range("20130101", periods = 6)
print(dates)
print("\n")
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list("ABCD"))
print(df)
print("\n")
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B" : pd.Timestamp("20230102"),
        "C" : pd.Series(1, index = list(range(4)), dtype="float32"),
        "D" : np.array([3] * 4, dtype="int32"),
        "E" : pd.Categorical(["test", "train", "test", "train"]),
        "F" : "foo",
    }
)
print(df2)
print("\n")
print(df2.dtypes)
