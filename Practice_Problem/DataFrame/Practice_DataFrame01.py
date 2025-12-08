import pandas as pd

df = pd.DataFrame([['KFC', 1000, 4.5], ['McDonald', 2000, 3.9], ['SchoolFood', 2500, 4.2]],
                  index = [0, 1, 2],
                  columns=['food', 'price', 'rating'])

