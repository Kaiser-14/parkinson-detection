import os

import pandas as pd
import scipy.io

# Initial name of each dataset
names = ['dataset', 'actidn', 'feat']

# Create data directories
if not os.path.exists('data'):
	os.makedirs('data')
	os.makedirs('data/dataset')
	os.makedirs('data/actidn')
	os.makedirs('data/feat')

# Loop through every file and convert .mat into .csv format
for root, dirs, files in os.walk('archive'):
	for file in files:
		for name in names:
			if file.startswith(name):
				print(file)
				dataset_mat = scipy.io.loadmat('archive/' + file)

				df_dataset = pd.DataFrame.from_dict(dataset_mat[file[:-4]])
				if name == 'dataset':
					df_dataset = df_dataset.rename(columns={0: 'x_accel', 1: 'y_accel', 2: 'z_accel', 3: 'x_omega', 4: 'y_omega', 5: 'z_omega', 6: 'label'})

				df_dataset.to_csv('data/' + name + '/' + file + ".csv", index=False)
				os.remove('archive/' + file)
				
os.rmdir('archive')
