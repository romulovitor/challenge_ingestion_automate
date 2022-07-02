import pandas as pd
import datetime as dt



def read_file():
    url = 'https://drive.google.com/uc?id=14JcOSJAWqKOUNyadVZDPm7FplA7XYhrU'
    df = pd.read_csv(url)
    return df


def convert_to_datetime(df):

    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

def include_process_time(df):
    df['process_time'] = dt.datetime.now()
    return df


def verify_data_status(df):
    max_value = df['process_time'].max()
    print(max_value)
    max_value = dt.datetime.now().date()
    if max_value == dt.datetime.today().date():
        print('The data was load today')
    else:
        print('The process was not executed today')


def group_by_week(df):
    df['week_number'] = df['datetime'].dt.strftime('%U')
    grp = df.groupby('region', observed=True)
    grp.agg({'week_number': 'mean'}, axis=0).apply(print)


def group_by_three_way(df):
    df_similar_origin = pd.DataFrame()
    df_similar_origin['origin_coord'] = df['origin_coord']
    df_similar_origin['destination_coord'] = df['destination_coord']
    df_similar_origin['time_hour'] = pd.DatetimeIndex(df['datetime']).hour
    df_similar_origin.groupby(['origin_coord', 'destination_coord', 'time_hour']).apply(print)

if __name__ == '__main__':
    df = read_file()
    df = convert_to_datetime(df)
    # df = group_by_three_way(df)
    # df = include_process_time(df)
    # verify_data_status(df)
    # print(df.to_markdown())
    group_by_week(df)
