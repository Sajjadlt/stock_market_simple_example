import pandas as pd
import requests


def updata_csv(apikey = "2HLFVCHVYZQO7BPO",symbol = "IBM"):
    url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_DAILY"
    params = {"function": function,"symbol": symbol,"apikey": apikey}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")

        df.to_csv("csv_data/data.csv", index_label="Date")
    
    else:
        print("error in receiving information")

def csv_read():
    file_path = "csv_data/data.csv"

    df = pd.read_csv(file_path)

    result = df.to_dict(orient='records')

    result = result[0:]

    result_dict = {row.pop(list(row.keys())[0]): row for row in result}
    
    return result_dict


