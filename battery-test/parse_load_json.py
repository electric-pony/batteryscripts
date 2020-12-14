import json
import csv

# enter file path of json file to convert
jsonfile = '/Users/roslynnricard/Google Drive/repo/20191201-143000.json'

# name file with cell serial number
csvfilename = 'SONY_VTC6A_2170_B.csv'

contents = ''
data_parsed = ''
config = ''
tags = ''

def parsejson():
    
    with open(jsonfile, 'r') as f:
        contents = f.read()

    data_parsed = json.loads(contents)

    # get cell and test details
    cell_type = data_parsed['config']['cell']
    current_sp = data_parsed['config']['discharge_current_A']
  
    tags = data_parsed['data'][1]['tags']
   
    #parse json and print to csv
    with open(csvfilename, 'w', newline='') as csvfile:
        fieldnames = ['cell_type','current_sp','time', 'current', 'voltage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader() 

        for i in range(len(data_parsed['data'])):
            time = data_parsed['data'][i]['time']
            current = data_parsed['data'][i]['fields']['current_a']
            voltage = data_parsed['data'][i]['fields']['voltage_v']
            writer.writerow({'cell_type': cell_type, 'current_sp' : current_sp, 'time': time, 'current' : current, 'voltage' : voltage})

if __name__ == "__main__":
    parsejson()