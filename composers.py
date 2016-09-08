import pandas as pd

medieval = pd.read_csv("medieval.txt", header = None)
medieval.columns = ['composer']
#print medieval.head()

medieval['era'] = 'medieval'
#print medieval.head()

renaissance = pd.read_csv("renaissance.txt", header = None)
renaissance.columns = ['composer']
renaissance['era'] = 'renaissance'
#print renaissance.head()

baroque = pd.read_csv("baroquecomposers.txt", header = None)
baroque.columns = ['composer']
baroque['era'] = 'baroque'
#print baroque.head()

classic = pd.read_csv("classcomposers.txt", header = None)
classic.columns = ['composer']
classic['era'] = 'classic'
#print classic.head()

romantic = pd.read_csv("romantic.txt", header = None)
romantic.columns = ["composer"]
romantic['era'] = 'romantic'
#print romantic.head()

twenty = pd.read_csv("composers_20thcentury.txt", header = None)
twenty.columns = ["composer"]
twenty['era'] = 'twentieth century'
#print twenty.head()

twentyfirst = pd.read_csv("composers_21st.txt", header = None)
twentyfirst.columns = ["composer"]
twentyfirst['era'] = 'twenty-first century'
#print twentyfirst.head()

## make one big dataframe combinding composers of all eras

composers_eras = [medieval, renaissance, baroque, classic, romantic, twenty, twentyfirst]
composers_eras = pd.concat(composers_eras)
print composers_eras
