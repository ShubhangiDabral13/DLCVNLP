import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',

'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})



def data_cleaning(df):
    """
    Creating the function which will perfrom all the data data_cleaning process.
    Param
    df:DataFrame whose cleaning we want to do
    """

    #Fill FlightNumber NaN values
    df.loc[df[df["FlightNumber"].isna()].index,"FlightNumber"] = [10055,10075]

    #Create a temperary DataFrame that contain 2 columns From and To created by splitting From_To column in df DataFrame
    dp = pd.DataFrame()
    dp[["From","To"]] = df.From_To.str.split("_",expand=True,)

    #capitalize only the first letter in strings of dp dataframe
    dp["From"] = dp["From"].str.capitalize()
    dp["To"] = dp["To"].str.capitalize()

    #concatenate temperary dataframe with df and then remove From_To column from df
    df = pd.concat([df,dp], axis=1)
    df.drop(columns = "From_To",axis = 1,inplace = True)



    #Expand the values of RecentDelays columns which are in list to to from different columns so that each value is in particular column
    df[["delay_1","delay_2","delay_3"]] = df.RecentDelays.apply(pd.Series)
    df.drop(columns = "RecentDelays",axis = 1,inplace = True)
    return df


cleaned_df = data_cleaning(df)
print(cleaned_df)
