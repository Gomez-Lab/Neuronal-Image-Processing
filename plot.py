import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

def createDictionary(self, pigID):
    '''Create dictionary containing all white pixel counts for a specific pigID'''
    # Path to the folder containing binary images
    folder_path = 'guided binary images'
    dayList = ['Day 3', 'Day 5', 'Day 5', 'Day 7', 'Day  15']
    woundLocs = ['L1', 'L2', 'C1', 'C2', 'C3', 'C4', 'C5', 'R1', 'R2']
    listDaysFile = ['D3', 'D5', 'D7', '15']

    data = {}
    for day in listDaysFile:
        dayDict = {}
        for loc in woundLocs:
            dayDict[loc] = 0
        data[day] = dayDict

    for filename in os.listdir(folder_path):
        if '1323F' in filename:
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
                        
    data_dict = data

    # Path to the folder containing binary images
    folder_path = 'guided binary images'
    #dayList = ['Day 3', 'Day 5', 'Day 5', 'Day 7', 'Day  15']
    woundLocs = ['L1', 'L2', 'C1', 'C2', 'C3', 'C4', 'C5', 'R1', 'R2']
    listDaysFile = ['D3', 'D5', 'D7', 'D15']

    data = {}
    for day in listDaysFile:
        dayDict = {}
        for loc in woundLocs:
            dayDict[loc] = 0
        data[day] = dayDict

    for filename in os.listdir(folder_path):
        if '1324F' in filename:
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
                        
    pig_1324F_dict = data

    # Path to the folder containing binary images
    folder_path = 'guided binary images'
    dayList = ['Day 3', 'Day 5', 'Day 5', 'Day 7', 'Day  15']
    woundLocs = ['L1', 'L2', 'C1', 'C2', 'C3', 'C4', 'C5', 'R1', 'R2']
    listDaysFile = ['D3', 'D5', 'D7', 'D15']

    data = {}
    for day in listDaysFile:
        dayDict = {}
        for loc in woundLocs:
            dayDict[loc] = 0
        data[day] = dayDict

    for filename in os.listdir(folder_path):
        if '1325F' in filename:
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
                        
    pig_1325F_dict = data

def plot(self):
    # outliers
    # 1325F D5 C3
    # 1323F D7 C2
    # 1325F D5 C1
    # 1324F D7 C1

    #input dataset from previous code
    data_dict = {'D3': {'L1': 235, 'L2': 1213, 'C1': 3984, 'C2': 784, 'C3': 0, 'C4': 0, 'C5': 0, 'R1': 0, 'R2': 0}, 'D5': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 4199, 'C4': 1106, 'C5': 0, 'R1': 2510, 'R2': 823}, 'D7': {'L1': 0, 'L2': 0, 'C1': 1073, 'C2': 0, 'C3': 3959, 'C4': 190, 'C5': 0, 'R1': 0, 'R2': 0}, '15': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 84, 'C4': 578, 'C5': 0, 'R1': 1243, 'R2': 1349}}
    pig_1324F_dict = {'D3': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 2537, 'C4': 2213, 'C5': 0, 'R1': 3322, 'R2': 198}, 'D5': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 1948, 'C4': 1689, 'C5': 0, 'R1': 4906, 'R2': 1013}, 'D7': {'L1': 2923, 'L2': 3965, 'C1': 0, 'C2': 6818, 'C3': 0, 'C4': 0, 'C5': 0, 'R1': 0, 'R2': 0}, 'D15': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 3052, 'C4': 1577, 'C5': 0, 'R1': 2254, 'R2': 3546}}
    pig_1325F_dict = {'D3': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 0, 'C4': 185, 'C5': 0, 'R1': 128, 'R2': 4106}, 'D5': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 2310, 'C3': 0, 'C4': 543, 'C5': 0, 'R1': 0, 'R2': 0}, 'D7': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 1763, 'C4': 2324, 'C5': 0, 'R1': 837, 'R2': 212}, 'D15': {'L1': 0, 'L2': 0, 'C1': 0, 'C2': 0, 'C3': 706, 'C4': 291, 'C5': 0, 'R1': 475, 'R2': 122}}

    #create dataframe for each day
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

    #combine dataframes
    df_combined = pd.concat([df, df2, df3], ignore_index=True)
    df_combined = df_combined[df_combined['Counts'] != 0]


    df_combined['Day'] = df_combined['Day'].replace('15', 'D15')
    df_combined['Day'] = df_combined['Day'].str.extract('(\d+)').astype(int)


    df_edge = df_combined[df_combined['WoundLocation'].isin(['L1', 'L2', 'R1', 'R2'])]
    df_center = df_combined[~df_combined['WoundLocation'].isin(['L1', 'L2', 'R1', 'R2'])]

    #plot box plots of dataframe
    plt.figure(figsize=(10, 6)) 
    ax = sns.boxplot(x='Day', y='Counts', data=df_edge, color='grey', width=0.4, boxprops=dict(facecolor='blue', alpha=0.2))
    sns.stripplot(x='Day', y='Counts', data=df_edge, color='blue', alpha=0.9, ax=ax, jitter=False)

    plt.title('Wound Edges', fontsize = 20)
    plt.xlabel('Day', fontsize = 18)
    ax.set_ylim([0, 7000])
    ax.tick_params(axis='x', labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    plt.ylabel('White Pixel Counts', fontsize = 18)
    plt.tight_layout()

    #save wound edges plot
    plt.savefig('Pixel Count Edges.jpg')

    plt.figure(figsize=(10, 6)) 
    ax = sns.boxplot(x='Day', y='Counts', data=df_center, color='grey', width=0.4, boxprops=dict(facecolor='red', alpha=0.2))
    sns.stripplot(x='Day', y='Counts', data=df_center, color='red', alpha=0.9, ax=ax, jitter=False)
    plt.title('Wound Centers', fontsize = 20)
    plt.xlabel('Day', fontsize = 18)
    ax.set_ylim([0, 7000])
    ax.tick_params(axis='x', labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    plt.ylabel('White Pixel Counts', fontsize = 18)
    plt.tight_layout()

    #save wound centers plot
    plt.savefig('Pixel Count Centers.jpg')
