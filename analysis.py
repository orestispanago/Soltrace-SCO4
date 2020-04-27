import pandas as pd


df = pd.read_csv("raydata.csv")

counts = df['Element'].value_counts()

abs_hits = counts.loc[-2]
mirror_hits = counts[counts.index>0].sum()


intercept_factor = abs_hits/mirror_hits