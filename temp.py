# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def new_damage(lists):
  conversion = {"M": 1000000, "B": 1000000000}
  for i in range(len(lists)):
      if lists[i] == 'Damages not recorded':
          continue
      else:
          for letter in lists[i]:
              if letter in conversion.keys():
                  lists[i] = float(lists[i][:-1]) * conversion[letter]
  return lists

# write your construct hurricane dictionary function here:
def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dic = {}
    i = 0
    while i in range(len(names)):
        for name in names:
            current_cane = {'Name': names[i],'Month': months[i],'Year': years[i],'Max Sustained Wind': max_sustained_winds[i], 'Area Affected': areas_affected[i],'Damage': damages[i], 'Deaths': deaths[i]}
            dic[name] = current_cane
            i += 1
    return dic
    
hurricane = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(test['Mitch'])

# write your construct hurricane by year dictionary function here:
def year_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dic = {}
    i = 0
    while i in range(len(names)):
        for year in years:
            current_cane = {'Name': names[i],'Month': months[i],'Year': years[i],'Max Sustained Wind': max_sustained_winds[i], 'Area Affected': areas_affected[i],'Damage': damages[i], 'Deaths': deaths[i]}
            if year in dic.keys():
                dic[year].append(current_cane)
            else:
                dic[year] = [current_cane]
            i += 1 
    return dic
 
#test1 = year_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(test1[1932])

# write your count affected areas function here:
def count_affect(areas_affected):
    dic = {}
    for places in areas_affected:
        for place in places:
            if place not in dic.keys():
                dic[place] = 1
            else:
                dic[place] += 1
    return dic

#test2 = count_affect(areas_affected)
#print(test2)

# write your find most affected area function here:
def most_affected_area(areas_affected):
    affected_times = count_affect(areas_affected)
    affected_times = {area: times for area, times in sorted(affected_times.items(), key=lambda item: item[1],reverse=True)}
    most_affected_area, times = list(affected_times.items())[0]
    return most_affected_area, times

#test3 = most_affected_area(areas_affected)
#print(test3)

# write your greatest number of deaths function here:
def most_death(names, deaths):
    death = {key:value for key,value in sorted(zip(names, deaths), key=lambda item:item[1], reverse = True)}
    most_death, number = list(death.items())[0]
    return most_death, number

#test4 = most_death(names,deaths)
#print(test4)

# write your catgeorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
death = {key:value for key,value in sorted(zip(names, deaths), key=lambda item:item[1], reverse = True)}

def mortality(dictionary):
    dic = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for cane in dictionary.keys():
        current_cane = dictionary[cane]
        if death == 0:
            dic[0].append(current_cane)
        elif 0 < death[cane] <= 100:
            dic[1].append(current_cane)
        elif 100 < death[cane] <= 500:
            dic[2].append(current_cane)
        elif 500 < death[cane] <= 1000:
            dic[3].append(current_cane)
        elif 1000 < death[cane] <= 10000:
            dic[4].append(current_cane)
        else:
            dic[5].append(current_cane)
    return dic

#test5 = mortality(death)
#print(test5[2])   
    
# write your greatest damage function here:
new_damages = new_damage(damages)
damages1 = {key:value for key,value in zip(names,new_damages)}

def greatest_damage(names,damages):
    damage = {key:value for key,value in zip(names,new_damages)}
    new = {}
    for cane in damage.keys():
        if damage[cane] != 'Damages not recorded':
            new[cane] = damage[cane]
    sort = {key: value for key,value in sorted(new.items(), key=lambda item:item[1], reverse=True)}
    most_cane, most_damage = list(sort.items())[0]
    return most_cane, most_damage
    
#test6 = greatest_damage(names,damages)
#print(test6)

# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def scale_damage(dictionary):
    dic = {0:[],1:[],2:[],3:[],4:[],5:[]}
    new = {}
    for cane in damages1.keys():
        if damages1[cane] != 'Damages not recorded':
            new[cane] = damages1[cane]
    for cane in new.keys():
        current_cane = new[cane]
        if damages1[cane] == 0:
            dic[0].append(current_cane)
        elif 0 < int(damages1[cane]) <= 100000000:
            dic[1].append(current_cane)
        elif 100000000 < int(damages1[cane]) <= 1000000000:
            dic[2].append(current_cane)
        elif 1000000000 < int(damages1[cane]) <=10000000000:
            dic[3].append(current_cane)
        elif 10000000000 < int(damages1[cane]) <=50000000000:
            dic[4].append(current_cane)
        else:
            dic[5].append(current_cane)
    return dic

test7 = scale_damage(damages1)
print(test7)



