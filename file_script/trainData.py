import os
import pandas as pd

data = pd.read_csv('data/Train.csv')

DataFrame = pd.DataFrame(data)
length = len(DataFrame)

width = DataFrame['Width']
height = DataFrame['Height']
classId = DataFrame['ClassId']
path = DataFrame['Path']
x1 = DataFrame['Roi.X1']
y1 = DataFrame['Roi.Y1']
x2 = DataFrame['Roi.X2']
y2 = DataFrame['Roi.Y2']
maxWidth = max(width)
maxHeight = max(height)
# print(DataFrame)

for i in range(length):
    centerX = (x1[i]+x2[i])/2
    centerY = (y1[i]+y2[i])/2
    norm_X = round(centerX/width[i],2)
    norm_Y = round(centerY/height[i],2)
    norm_width = round(width[i]/maxWidth,2)
    norm_height = round(height[i]/maxHeight,2)

    if norm_X>1 or norm_Y>1 or norm_width>1 or norm_height>1:
        print(f'Check this line {i} {norm_X} {norm_Y} {norm_width} {norm_height}')
        break
    dataToWrite = f'{classId[i]} {norm_X} {norm_Y} {norm_width} {norm_height}'
    print(dataToWrite)
    
    realPath = path[i]
    textPath = realPath.replace('png','txt')
    filePath = f'data/{textPath}'

    directory = os.path.dirname(filePath)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filePath, 'w') as file:
        file.write(dataToWrite)

    print(f'File {i} done')





''' Annotated data format --> 
Class_number Center_X Center_Y Width Height
      0          45      55      29     67
'''