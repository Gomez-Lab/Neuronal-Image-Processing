import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

def createDictionary(self, pigID):
    '''Create dictionary containing all white pixel counts for a specific pigID'''
    # Path to the folder containing binary images
    folder_path = 'binary images'
    woundLocs = ['L1', 'L2', 'C1', 'C2', 'C3', 'C4', 'C5', 'R1', 'R2']
    listDaysFile = ['D3', 'D5', '15']

    data = {}
    for day in listDaysFile:
        dayDict = {}
        for loc in woundLocs:
            dayDict[loc] = 0
        data[day] = dayDict

    for filename in os.listdir(folder_path):
        if pigID in filename:
            for day in listDaysFile:
                for loc in woundLocs:
                    if day in filename and loc in filename:
                        image_path = os.path.join(folder_path, filename)
                        binary_image = cv2.imread(image_path, 0)

                        # Find the total number of white pixels
                        whitePixel = cv2.countNonZero(binary_image)
                        imgSize = binary_image.size

                        #calcualte the density
                        density = whitePixel/imgSize

                        data[day][loc] = whitePixel
                        
    return data

def plot(self):
    data_dict = {'D3': {'L1': 391, 'L2': 1092, 'C1': 3033, 'C2': 833, 'C3': 0, 'C4': 0, 'C5': 0, 'R1': 0, 'R2': 0}, 'D5': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 2079, 'C4': 952, 'C5': 0, 'R1': 2144, 'R2': 923}, '15': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 135, 'C4': 570, 'C5': 0, 'R1': 1123, 'R2': 1452}}
    pig_1324F_dict = {'D3': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 2009, 'C4': 2008, 'C5': 0, 'R1': 2998, 'R2': 526}, 'D5': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 1779, 'C4': 1136, 'C5': 0, 'R1': 4808, 'R2': 1130}, 'D7': {'L1': 3592, 'L2': 3304, 'C1': 4462, 'C2': 6031, 'C3': 0, 'C4': 0, 'C5': 0, 'R1': 0, 'R2': 0}, 'D15': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 1811, 'C4': 1140, 'C5': 0, 'R1': 2582, 'R2': 3063}}
    pig_1325F_dict = {'D3': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 10, 'C4': 177, 'C5': 0, 'R1': 218, 'R2': 4063}, 'D7': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 1701, 'C4': 2176, 'C5': 0, 'R1': 915, 'R2': 409}, 'D15': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 730, 'C4': 269, 'C5': 0, 'R1': 398, 'R2': 292}}


    data = []
    for day, locations in data_dict.items():
        for location, count in locations.items():
            data.append(['1323F', day, location, count])

    df = pd.DataFrame(data, columns=['Pig', 'Day', 'WoundLocation', 'Counts'])



    data_2 = []
    for day, locations in pig_1324F_dict.items():
        for location, count in locations.items():
            data_2.append(['1324F', day, location, count])
            
            
    df2 = pd.DataFrame(data_2, columns=['Pig', 'Day', 'WoundLocation', 'Counts'])



    data_3 = []
    for day, locations in pig_1325F_dict.items():
        for location, count in locations.items():
            data_3.append(['1325F', day, location, count])
            
            
    df3 = pd.DataFrame(data_3, columns=['Pig', 'Day', 'WoundLocation', 'Counts'])


    df_combined = pd.concat([df, df2, df3], ignore_index=True)
    df_combined = df_combined[df_combined['Counts'] != 0]


    df_combined['Day'] = df_combined['Day'].replace('15', 'D15')
    df_combined['Day'] = df_combined['Day'].str.extract('(\d+)').astype(int)


    df_edge = df_combined[df_combined['WoundLocation'].isin(['L1', 'L2', 'R1', 'R2'])]
    df_center = df_combined[~df_combined['WoundLocation'].isin(['L1', 'L2', 'R1', 'R2'])]


    plt.figure(figsize=(10, 6)) 
    ax = sns.boxplot(x='Day', y='Counts', data=df_edge, color='grey', width=0.4, boxprops=dict(facecolor='blue', alpha=0.2))
    sns.stripplot(x='Day', y='Counts', data=df_edge, color='blue', alpha=0.9, ax=ax, jitter=False)

    plt.title('White Pixel Counts by Day in Wound Edges', fontsize = 20)
    plt.xlabel('Day', fontsize = 18)
    ax.set_ylim([0, 7000])
    ax.tick_params(axis='x', labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    plt.ylabel('White Pixel Counts', fontsize = 18)
    plt.tight_layout()

    plt.savefig('Pixel Count Edges.jpg')

    plt.figure(figsize=(10, 6)) 
    ax = sns.boxplot(x='Day', y='Counts', data=df_center, color='grey', width=0.4, boxprops=dict(facecolor='red', alpha=0.2))
    sns.stripplot(x='Day', y='Counts', data=df_center, color='red', alpha=0.9, ax=ax, jitter=False)
    plt.title('White Pixel Counts by Day in Wound Centers', fontsize = 20)
    plt.xlabel('Day', fontsize = 18)
    ax.set_ylim([0, 7000])
    ax.tick_params(axis='x', labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    plt.ylabel('White Pixel Counts', fontsize = 18)
    plt.tight_layout()

    plt.savefig('Pixel Count Centers.jpg')
