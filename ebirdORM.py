from ebird.api import get_observations
import pandas as pd
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

api_key = 'your-api-key-here'

def job():
    records = get_observations(api_key, 'CA-ON', back = 30)
    df = pd.DataFrame(records)
    df.to_csv('C:/Users/Owner/Desktop/Python Scripts/outputs/sar_observations' + today + '.csv')

print('done!')
