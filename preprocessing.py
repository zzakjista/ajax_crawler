from options import args
import pandas as pd
import numpy as np

class preprocessor:

    def __init__(self,args,data):
        self.args = args
        self.theme = args.theme
        self.data = data

    def preprocess(self):
        if self.theme == "가정통신문":
            return self.preprocess_letter_notice()
        elif self.theme == "공지사항":
            return self.preprocess_letter_notice()
        elif self.theme == "학교급식":
            return self.preprocess_bob()
    
    def preprocess_letter_notice(self):
        df = pd.DataFrame(self.data,columns=['date','name','title','content'])
        df['content'] = df['content'].str.replace('\n','')
        df['content'] = df['content'].str.replace('\t','')
        df['content'] = df['content'].str.replace('\r','')
        return df

    def preprocess_bob(self):
        self.remove_empty()
        df = self.concat_data()
        return df

    def concat_data(self):
        df = pd.DataFrame()
        for i in range(len(self.data)):
            tmp = pd.DataFrame(self.data[i])
            df = pd.concat([df,tmp],axis = 0)
        df.columns=['category','date','title','menu','kcal']
        return df

    def remove_empty(self):
        bob = []
        for i in range(len(self.data)):
            if self.data[i] != []:
                bob.append(self.data[i])
        self.data = bob
            