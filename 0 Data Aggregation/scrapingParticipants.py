import requests
import zipfile
import io
import os
import pandas as pd
import xml.etree.ElementTree as et

#global variables
dates = []
participants = []
id = 9 # Id 9 for 2016-01-01
filereading = True
outputPath ='../00 Data/marketParticipants.csv'

#  save data to csv
def saveToCSV(date, part, path):
    df = pd.DataFrame(columns=['date','participants'])
    df['date'] = date
    df['participants'] = part
    df.to_csv(path,index=False,sep=',')

if filereading:
    while id < 9999:
        url = 'https://www.acer-remit.eu/portal/register-download?fileType=XML&euregId=' + `id`
        response = requests.get(url)
        # extract & save xml files
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip:
            zip.extractall('../00 Data/marketParticipantsMonthly')
            zip.close()
        if id < 30: #october 2017
            id = id + 1
        #november 2016 has no file!
        elif id == 30:
            id = 1650  #december 2017
        else:
            id = 9999

script_dir = os.path.dirname(__file__) # absolute dir this script is in
found = False
delete = 0
for c in reversed(script_dir):
     if not c == '/' and found <> True:
         delete = delete + 1
     else:
        found = True
script_dir = script_dir[0:(len(script_dir)-delete)]
rel_path = "00 Data/marketParticipantsMonthly" #relative path for XML files
path = os.path.join(script_dir, rel_path)
filelist = os.listdir(path)
filelist.sort()
for filename in filelist:
    number = 0
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    tree = et.parse(fullname)
    root = tree.getroot()
    for atype in root.findall('.//state'):
        if atype.text == 'Germany':
            number = number + 1
    date = filename[3:13]
    dates.append(date)
    participants.append(number)

saveToCSV(dates, participants, outputPath)
