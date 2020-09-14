import subprocess
import os
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime

import requests
import json

def get_johns_hopkins():
    git_pull = subprocess.Popen('C:/Program Files/Git/usr/bin/git pull', cwd = os.path.dirname('../data/raw/COVID-19/'), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    (out, error) = git_pull.communicate()
    print("Error  :" + str(error))
    print("out :" + str(out))
    

def get_current_data_germany():
    ''' Get current data from germany, attention API endpoint not too stable
        Result data frame is stored as pd.DataFrame
    '''
    # 16 states
    #data=requests.get('https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/Coronaf%C3%A4lle_in_den_Bundesl%C3%A4ndern/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')

    # 400 regions / Landkreise
    data=requests.get('https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')

    json_object=json.loads(data.content)
    full_list=[]
    for pos,each_dict in enumerate (json_object['features'][:]):
        full_list.append(each_dict['attributes'])

    pd_full_list=pd.DataFrame(full_list)
    pd_full_list.to_csv('C:/Users/admin/ads_covid-19/data/raw/NPGEO/GER_state_data.csv',sep=',')
    print(' Number of regions rows: '+str(pd_full_list.shape[0]))

if __name__ == '__main__':
    get_johns_hopkins()
    get_current_data_germany()