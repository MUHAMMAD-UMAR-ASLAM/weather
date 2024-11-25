from file_reader import read_file

def find_minimumm_temperature(year):
    min= float('inf')
    months=['Jan','Feb','Mar',"Apr",'May',"Jun","Jul",'Aug','Sep','Oct','Nov','Dec']    
    for month in months:
        file_path = 'weatherfiles/Murree_weather_'+str(year)+'_'+month+'.txt'

        file_content = read_file(file_path)
        data=file_content[1:]
        for row in data:
            if row[3]!="":
                if min>float(row[3]):
                    min=float(row[3])            
    
    return min

find_minimumm_temperature(2011)