def archiver():
   
    import pandas as pd
     
    df = pd.read_json("https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json")
    df.drop(df.iloc[:, 2:4], inplace=True, axis=1)
    df = df.drop(df.index[0])
    df.columns = ['Date', '3hrKp']
    df[['Date','Time']] = df.Date.str.split(" ",expand=True)
    cols = ['Date', 'Time', '3hrKp']
    df['Time'] = df['Time'].str.split(':').str[0] + df['Time'].str.split(':').str[1] # clean up time - fewer zeros
    df=df[cols]
    df = df.iloc[-1:] # latest observation
    
    from time import gmtime, strftime
    
    now_UTC = strftime('%H%M', gmtime()) + " UTC"
    
    print(f'The current UTC time is {now_UTC}.')
    
    from datetime import datetime
    now_local=datetime.now().strftime('%H%M') + ' MST'
    
    print(f'The current local time is {now_local}.')
    
    print(f"The latest 3 hrly Kp observed on {df['Date'].iloc[-1]} at {df['Time'].iloc[-1]} was {df['3hrKp'].iloc[-1]}")
    
    import sqlite3

    conn = sqlite3.connect('3hrKp_archive.db')
    #cur = conn.cursor()
    
    df.to_sql('3hrKp', conn, if_exists='append')
    
    conn.close()
      
import schedule
import time
    
schedule.every(18000).seconds.do(archiver) # archives every 5 hours

while 1:
    schedule.run_pending()
    time.sleep(1)
        
        
    
