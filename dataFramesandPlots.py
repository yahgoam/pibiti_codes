import pandas as pd

colnames = ['index', 'humidity', 'temp1','pressure','temp2', 'light_lvl']
data = pd.read_csv("logFile.csv",names=colnames, header=None)
data = data.set_index(['index'],drop=True)

sensor_1 = data.loc[data.index == 1]
sensor_2 = data.loc[data.index == 2]

new_index = [i for i in range(len(sensor_1.index))]
new_index2 = [i for i in range(len(sensor_2.index))]
sensor_1['new_index'] = new_index
sensor_2['new_index'] = new_index2

sensor_1 = sensor_1.set_index(['new_index'], drop = True)
sensor_2 = sensor_2.set_index(['new_index'], drop = True)