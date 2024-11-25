from file_reader import read_file

def find_minimumm_temperature(year):
    max_value= float('-inf')
    months=['Jan','Feb','Mar',"Apr",'May',"Jun","Jul",'Aug','Sep','Oct','Nov','Dec']    
    for month in months:
        file_path = 'weatherfiles/Murree_weather_'+str(year)+'_'+month+'.txt'

        file_content = read_file(file_path)
        data=file_content[1:]
        for row in data:
            if row[1]!="":
                if max_value<float(row[1]):
                    max_value=float(row[1]) 
              
    
    return max_value

find_minimumm_temperature(2011)