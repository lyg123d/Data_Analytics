import pandas as pd

list_data= [10, 20, 30, 40, 50]
sr = pd.Series(list_data, index=['가', '나', '다', '라', '마'])


print(sr[['나','라']])
