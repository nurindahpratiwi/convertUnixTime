from time import strftime
import pandas as pd
from datetime import datetime

def convertTime(df):
    #change columns with your desire columns names: ["columns_name"]
    sel_column = df[columns]
    #if your file contains missing value, I set to replace it with white space
    sel_col = sel_column.fillna(' ')
    for files in sel_col:
        if files != ' ':
            value_as_int = int(files)
            #this line is important to convert Unix time to Datetime
            currTime = datetime.fromtimestamp(value_as_int).strftime('%d-%m-%Y %H:%M:%S')
            print (currTime)
        else:
            print ('NULL')

filename = pd.read_csv("your/path/file")
result = convertTime(filename)
print (result)
