import pandas as pd
import sys

# 5poses results convertion to pandas table
filedat = sys.argv[1]
out = sys.argv[2]

print(filedat)
print(out)

df = pd.read_csv(filedat)

# determino los indices de las filas con el menor valor de score, dentro de las moleculas agrupadas por "name"
indices = df.groupby('name')['score'].idxmin()

print df.groupby('name')['score'].idxmin()

# obtengo las filas originales de la tabla, que corresponden a los menores valores de score para cada molecula
newdf = df.loc[indices]

#newdf = newdf.sort_values(by=['score'])

newdf.to_csv(out, sep='\t')
