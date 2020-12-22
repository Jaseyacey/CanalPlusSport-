import datetime
import csv
import pendulum
import requests
from tabulate import tabulate
import pandas as pd
import numpy as np

api_url = "https://secure-webtv-static.canal-plus.com/metadata/cpfra/all/v2.2/globalchannels.json"
response = requests.get(api_url).json()

tv_programme = {
    channel["name"]: [
        [
            e['title'],
            e['subTitle'],
            pendulum.parse(e['timecodes'][0]['start']
                           ).time().strftime("%H:%M"),
        ] for e in channel["events"]
    ] for channel in response["channels"]
}


print(tabulate(
    tv_programme["BEIN SPORTS MAX 9"],
    headers=["Title", "Subtitle", "Time", "Duration"],
    tablefmt="csv",
))
df = pd.DataFrame(tv_programme["BEIN SPORTS MAX 9"],
                  columns=["Title", "Subtitle", "Time", ])
df.to_csv("bein_sports_max_nine.csv", index=False)

# print("\n".join(sorted(list(tv_programme.keys()))))
