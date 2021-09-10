import os
import csv

class PreprocessData:

    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data_original_dir = self.data_dir + 'original/'
        self.data_processed_dir = self.data_dir + 'processed/'

    def preprocess(self, dataset_name):

        if dataset_name == 'bean_disease_uganda':
            None
        
        if dataset_name == 'carrot_weeds_germany':
            None

        if dataset_name == 'carrot_weeds_macedonia':
            None

        if dataset_name == 'rangeland_weeds_australia':
            dataset_dir = self.data_original_dir + dataset_name + '/'
            labels_dir = dataset_dir + 'labels/'
            labels_path = labels_dir + 'labels.csv'
            labels = []
            labels_unique = []

            # Make directories with class names
            with open(labels_path) as f:
                next(f)
                labels = [row.split(',')[2] for row in f]

            # Read through list, keep only unique classes, and create directories for each class name
            for label in labels:
                if label not in labels_unique:
                    labels_unique.append(label)
                    os.mkdir(labels_dir + label)

            # Move files to folder with correct class names