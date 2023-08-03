from options import args
import pandas as pd
import numpy as np

class save_file:
    def __init__(self,args,df):
        self.args = args
        self.theme = args.theme
        self.df = df
        self.save_path = args.save_path
        self.file_type = args.file_type
        self.file_path = f'{self.save_path}/{self.theme}'

    def save(self):
        if self.file_type == 'json':
            self.save_json()
        elif self.file_type == 'excel':
            self.save_excel()
        elif self.file_type == 'csv':
            self.save_csv()
        elif self.file_type == 'pickle':
            self.save_pickle()
        elif self.file_type == 'feather':
            self.save_feather()
        elif self.file_type == 'parquet':
            self.save_parquet()
        elif self.file_type == 'hdf':
            self.save_hdf()
        return

    # json
    def save_json(self):
        self.df.to_json(f'{self.file_path}.json',orient='records',force_ascii=False)
        return

    # excel
    def save_excel(self):
        self.df.to_excel(f'{self.file_path}.xlsx',index=False,encoding='utf-8-sig')
        return
    
    # csv
    def save_csv(self):
        self.df.to_csv(f'{self.file_path}.csv',index=False,encoding='utf-8-sig')
        return
    
    # pickle
    def save_pickle(self):
        self.df.to_pickle(f'{self.file_path}.pickle')
        return
    
    # feather
    def save_feather(self):
        self.df.to_feather(f'{self.file_path}.feather')
        return

    # parquet
    def save_parquet(self):
        self.df.to_parquet(f'{self.file_path}.parquet')
        return

    # hdf
    def save_hdf(self):
        self.df.to_hdf(f'{self.file_path}.hdf',key='data',mode='w')
        return
    
    
