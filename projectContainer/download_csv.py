#!/usr/bin/env python

from datasets import load_dataset
import re
import pandas as pd


def process_file(name_of_path):
    """
    Opens, reads, and closes a given file.
    Returns the contents of this file as a string.
    """
    with open(name_of_path, encoding="utf-8") as file:
        data_path_cleaned = file.read()

    return data_path_cleaned


def strip_csv_link(data):
    """
    Finds dataset name from data link via regex.
    Returns a string of the dataset to search for on Hugging Face.
    """
    penult_word = 'datasets/'

    # regex to find string after 'datasets/'
    # may need some heavier testing - could be broken if there are weird file formats
    r = re.search(f"({penult_word})([A-Za-z0-9_-]+)", data)[2]

    return r


def load_data(repo_name):
    """
    Loads data from Hugging Face.
    Returns this dataset
    """    
    # write a function that loads a dataset with repo name and uses the default parameter for name
    # TODO #1 find a way to automate the name parameter
    dataset = load_dataset(path=repo_name)#, name='boolq')
 

    print('-'*100)
    print(f"dataset {repo_name} successfully loaded!")
    print('-'*100)

    return dataset


def join_splits(dataset):
    """
    Hugging Face downloads datasets in train, test, val splits, so this function joins them all into one data structure.
    Returns a DataFrame of the entire dataset.
    """

    # get each split of dataset from dictionary
    train = dataset.get('train')
    test = dataset.get('test')
    val = dataset.get('validation')

    # convert each to df
    train, test, val = pd.DataFrame(train), pd.DataFrame(test), pd.DataFrame(val)

    # join them all into one big dataframe
    df = train.append(test)
    df = df.append(val)

    return df




def main(text_file):
    """
    Driver function of the program.
    Calls other functions to read, preprocess, and search for user-given dataset.
    Returns final dataset, to be passed back into bash script.
    """
    # call first two functions to find name of repo from user input
    data = process_file(text_file)
    repo_name = strip_csv_link(data)
    
    print('-'*100)
    print("data successfully cleaned")
    print('-'*100)

    # call simple function to load data, passing in repo name found in previous function
    dataset = load_data(repo_name)

    # join each split (train, test, val) into one dataframe
    df = join_splits(dataset)

    return df

# call main function, export dataframe as a csv file
final_df = main('data.txt')
final_df.to_csv('downloaded_data.csv')