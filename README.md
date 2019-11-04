# classification_project
Determining if a house would sell for above average price.

-[Data](#Data)
    *[Source](#Source)
    *[Features](#Features) 
-[EDA](#EDA)
    *[Visualizations](#Viz)
-[Modeling](#Modeling)
    *[Choosing The Model](#ModChoice)
    *[Interpretation of the Model](#ModInterp)
-[Conclusions](#Conclu)
-[Next Steps](#Future)

## Data <a name="Data"></a>
### Source <a name="Source></a>
I obtained my data from [NYCOpenData](https://opendata.cityofnewyork.us/). I used their API to gather data on housing sales, and chose to move forward with housing sales in Brooklyn in 2015 (the most recent year they had).
My objective for this project was to classify the sale price, to predict if it would be either above or below the average sale price in that borough.

### Features <a name="Features"></a>
The data came with lot of great information, but not everything was in a useable format. Some of the features that I looked into for this model were:
- Borough
- Block
- Building Class
- Tax Class
- Apartment Number
- Zip Code
- Number of Residential Units
- Number of Commercial Units
- Land sq ft
- Gross sq ft
- Year Built
- Sale Date
- Address

## EDA <a name="EDA"><\a>