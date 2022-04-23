# 安裝套件
import twint
# Use to handle notebook & Runtime Error
# 允許是事件迴圈已經在執行的情況下，再執行一次事件迴圈
import nest_asyncio
nest_asyncio.apply()

import os
import datetime as dt

# 如果要將資料存成csv
import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
# function
def twint_search(search_term, since, until, save_path):
    c = twint.Config()
    c.Search = search_term
    # Language -> only English
    c.Lang = "en"
    # Location
    # c.Location = 
    c.Since = since.strftime('%Y-%m-%d %H:%M:%S')
    c.Until = until.strftime('%Y-%m-%d %H:%M:%S')
    # Limit for each data
    # c.Limit = 10000
    c.Hide_output = True
    # store data as csv
    c.Store_csv = True
    # set path to save data
    c.Output = save_path
    twint.run.Search(c)
    
def twint_search_loop(search_term, start_date, end_date, save_dir):
    # create file to save data
    try:
        os.makedirs(os.path.join(os.getcwd(),save_dir,search_term))
        print(f'Successfully created the directory {os.path.join(os.getcwd(),save_dir,search_term)}')
    except FileExistsError:
        print(f'Directory {os.path.join(os.getcwd(),save_dir,search_term)} already exists')
    
    date_range = pd.date_range(start_date, end_date)
    
    for single_date in date_range:
        since = single_date
        until = single_date + dt.timedelta(days=1)
        save_path = os.path.join(save_dir, search_term, f'{single_date:%Y%m%d}.csv')
        print(f"Searching for tweets containing '{search_term}' from {single_date:%Y-%m-%d} and saving into {save_path}")
        twint_search(search_term, since, until, save_path)

# Keyword -> can use OR to search multiple words
search_term = 'Covid OR COVID19 OR COVID-19 OR Covid_19 OR coronavirus OR CORONA OR lockdown OR vaccine OR CoronaVirusUpdate'
# Scrape how many dates' data
# official
start_date = dt.datetime(2019, 11, 1)
end_date = dt.datetime(2022, 3, 31)
# dir to save data
save_dir = 'D:/Twitter data/raw/'

# run search
twint_search_loop(search_term, start_date, end_date, save_dir)