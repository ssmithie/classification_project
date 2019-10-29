# strip the odd punctuation from the column names, and change spaces for underscores
df.columns = df.columns.str.strip('\n')
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace("-", "_")
# get rid of any oddly low prices (10,000/25,000 rows)
indexname = df[df['SALE PRICE'] <= 50000].index
df.drop(indexname, inplace=True)
#turn the date sold into season
df['SALE SEASON'] = df['SALE DATE'].apply(lambda dt: (dt.month%12 + 3)//3)
#get rid of odd punctuation in some columns
df['BUILDING CLASS CATEGORY'] = df['BUILDING CLASS CATEGORY'].str.rstrip()
df['APARTMENT NUMBER'] = df['APARTMENT NUMBER'].str.rstrip()
#turn the blank values into Nan
df.loc[df['APARTMENT NUMBER'] == '', 'APARTMENT NUMBER'] = None
# drop the ease-ment column, no actual data
df.drop(['EASE-MENT'], axis=1, inplace=True)
# create a column of the means of the zips
zip_mean = df.groupby(['ZIP_CODE']).SALE_PRICE.mean().to_dict()
df['zip_mean'] = [zip_mean[x] for x in df['ZIP_CODE']]
# create another column that codes for whether or not the sale price is above the zip mean
df['above_mean'] = np.where(df['SALE_PRICE'] >= df['zip_mean'], 1, 0)
# dealing with the missing zip values, two I could get from block, one I just dropped
df.drop(df.loc[df['BLOCK'] == 3880].index, inplace=True)
df.loc[df['BLOCK'] == 8590, 'ZIP_CODE'] = 11234
# bin the years in 20yr blocks
bins = pd.IntervalIndex.from_tuples([(1800,1900), (1901,1920), (1921, 1940), (1941, 1960), (1961, 1980), (1981, 2000), (2001, 2016)])
df['year'] = pd.cut(df['YEAR_BUILT'], bins)
# bin apartment numbers, decide that if none then it's likely the entire building, put anything with
# PH into a category, and everything else in another block
cleanup_nums = {'APARTMENT_NUMBER':     {'4PH': 2,'PH-D': 2,'5PH': 2, 'PH B': 2,'PHB1': 2,'PH-A': 2, 'PH-B': 2,'PHA': 2,'PHF': 2,'PHN': 2,'PHB': 2,'PH8': 2,'PH': 2,'PH1': 2,'PH2': 2,'PH4': 2,'PH3': 2,'PH1A': 2,'PH3B': 2,'PH2A': 2, 'PH2B': 2, 'PH2D': 2, 'PH2E': 2, 'PH2F': 2,'PH1C': 2}}
df.replace(cleanup_nums, inplace=True)
df.APARTMENT_NUMBER.fillna(0, inplace=True)
def is_string(x):
    if type(x) == int:
        return x
    else: 
        x = 1
        return x
    
df['APARTMENT_NUMBER'] = df['APARTMENT_NUMBER'].apply(is_string)
# drop some more columns
df.drop(['BOROUGH'], axis=1, inplace=True)