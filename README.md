# Parkinson Detection

## Information

### Dataset
For the development of the Parkinson's prediction, only one of the 3 available datasets was used, since they contained enough information to develop a viable prediction model.

The data required for the code is in the 'data/dataset' folder, but the download link is at the following:

https://www.kaggle.com/giofra/simulation-of-parkinson-movement-disorders

### Context
Parkinson's disease is associated with symptoms of movement disorders, such as tremor, and bradykinesia. Through an analysis of the movements of people with the disease, we can predict serious episodes of the disease and anticipate help.

These signals have been recorded with the purpose of implementing an algorithm that can recognize and analyse movement singularities of degenerative diseases, such as Alzheimer or Parkinson, and gait disorders in elderly people. The Inertial sensors (a triaxial accelerometer and a triaxial gyroscope) have been settled on the top of a right slipper placed in the lower limb have
been employed. That allows to obtain a collection of data in order to track human motions in daily life with less intrusion.

### Content
The signals are relative to ten volunteers that have simulated the following seven movements:
-Freezing of gait (1)
-Bradykinesia (2)
-Sitting with tremor (3)
-Ataxic gait (4)
-Myopathic gait (5)
-Muscle atrophy (6)
-Not pathological gait (7)
To each one of them is associated a label (i.e. the number into the bracket).
The recording protocol establishes that for each subject, each movement is repeated 10 times and for each time the recording lasts 20 seconds. The signals have been captured with a sample frequency of 100 Hz.

[comment]: <> (#### actidnX.mat)

[comment]: <> (This is the response vector relative to the features matrix 'feat1')

#### dataset_X.mat
These matrices are relative to the recorded data for every subject of the test. Specifically, 10 different people have simulated the movements to complete each dataset.

They contain 7 columns:
-the recording of the acceleration signal along x-axis
-the recording of the acceleration signal along y-axis
-the recording of the acceleration signal along z-axis
-the recording of the angular velocity signal along x-axis
-the recording of the angular velocity signal along y-axis
-the recording of the angular velocity signal along z-axis
-the vector of the labels associated to each kind of movement

[comment]: <> (#### featX.mat)

## Code

### Requirements

* Python
* TensorFlow
* Keras
* Scipy
* Sklearn
* Seaborn
* Matplotlib

### Preparation
The data provided through the link was in .mat format. To facilitate integration with Python, I developed the preparation.py code to convert them to csv format. Likewise, the datasets were divided into folders to facilitate their understanding and division.

If you downloaded from the link, execute the code in order to have everything according to the subsequent analysis.

### Execution
Run the parkinson_analysis.ipynb line by line to execute the whole code.

### Results

In the following table we can observe the results obtained throughout all the models developed. We include those sections such as the use of dataset individually, as well as searching for label filtering or complete dataset.

When we use a single dataset for training, the choice of the model lies between the optimal and the powerful, since they obtain similar values. In this case, I would even opt for the optimal one since it is a simpler model and we could obtain results more efficiently. However, when we use the set of datasets (except Nirvana in this notebook for training) perhaps we could opt for the powerful, since although it does not exceed much, but we get a good recovery of accuracy of values.

On the other hand, with the label filtering we found that we significantly increased the accuracy of the models. It is difficult for the two simple models to train with the data set. With the most powerful architecture, we achieve 70% accuracy for external data, with outstanding results.

As a future objective, I consider that the neural network architectures are established, so it would be more useful to group the different labels, since some of the movements may be similar to each other, and we could increase efficiency in the models.

| . | Training | Validation | External |
| :---: | :---: | :---: | :---: |
| Individual dataset |  |
| Simple | .534 | .531 | .360 |
| Improved | .651 | .648 | .448 |
| Optimal | .798 | .776 | .511 |
| Powerful | .832 | .783 | .531 |
| Filtering labels (ind.) |  |
| Simple | .559 | .560 | .397 |
| Improved | .707 | .706 | .464 |
| Optimal | .842 | .827 | .552 |
| Powerful | .855 | .825 | .557 |
| Complete dataset |  |
| Simple | .330 | .330 | .331 |
| Improved | .383 | .384 | .380 |
| Optimal | .647 | .642 | .622 |
| Powerful | .682 | .669 | .656 |
| Filtering labels (compl.) |  |
| Simple | .389 | .389 | .390 |
| Improved | .420 | .420 | .418 |
| Optimal | .703 | .698 | .680 |
| Powerful | .736 | .723 | .708 |
