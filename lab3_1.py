import pandas as pd
import numpy as np
mtcars = pd.read_csv('mtcars.csv')
najveca_potrosnja = mtcars .sort_values(by=['mpg']).head(5)
print(najveca_potrosnja)

cilindri_osam = mtcars[mtcars['cyl'] == 8].sort_values(by=['mpg']).tail(5)
print(cilindri_osam)


cilindri_sest = mtcars[mtcars['cyl'] == 6]['mpg'].mean()
print("Srednja potrosnja sestaka je: ",cilindri_sest)

cil_cetiri_tezina =  mtcars[(mtcars['cyl'] == 4) & (mtcars['wt'] * 1000 >= 2000) & (mtcars['wt'] * 1000 <= 2200)]
srednja_cetiri = cil_cetiri_tezina['mpg'].mean()
print(srednja_cetiri)


broj_mjenjaca = mtcars['am'].value_counts()
print(f"Broj automobila s automatskim mjenjačem: {broj_mjenjaca.get(0, 0)}")
print(f"Broj automobila s ručnim mjenjačem: {broj_mjenjaca.get(1, 0)}")

auto_preko_sto = mtcars[(mtcars['am'] == 0) & (mtcars['hp'] >= 100)]
broj_jakih=len(auto_preko_sto)
print("Broj automatskih s preko 100ks je ",broj_jakih)

mtcars['wt_kg'] = mtcars['wt'] * 1000 * 0.453592
print(mtcars[['car', 'wt_kg']])  
