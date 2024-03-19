import os
import pickle
import json 
import random
import csv

def read_json_file(filepath):
    with open(filepath) as infile:
        data_dict = json.load(infile)
    return data_dict

def save_json_file(filepath, data_dict):
    with open(filepath, "w") as outfile:
        json.dump(data_dict, outfile)

def load_pickle_file(filepath):
    with open(filepath, 'rb') as infile:
        pickle_data = pickle.load(infile)
    return pickle_data

def save_pickle_file(filepath, pickle_data):
    with open(filepath, 'wb') as outfile:
        pickle.dump(pickle_data, outfile)

def dump_jsonl(data, output_path, append=False):
    """
    Write list of objects to a JSON lines file.
    """
    mode = 'a+' if append else 'w'
    with open(output_path, mode, encoding='utf-8') as f:
        for line in data:
            json_record = json.dumps(line, ensure_ascii=False)
            f.write(json_record + '\n')
    print('Wrote {} records to {}'.format(len(data), output_path))

def load_jsonl(path):
    data=[]
    with open(path, 'r', encoding='utf-8') as reader:
        for line in reader:
            data.append(json.loads(line))
    return data 

def merge_jsonl_files(data_dir_list, subsample  = -1):

    final_data = []
    for data_dirpath in data_dir_list:
        final_data+=load_jsonl(data_dirpath)

    if subsample !=-1:
        random.shuffle(final_data)
        final_data = final_data[:subsample]
    return final_data

def dump_csv_data(header_data, content_data, filepath, delimeter=","):
    with open(filepath, "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=delimeter)
        csv_writer.writerow(header_data)
        for data_item in content_data:
            csv_writer.writerow(data_item)

def append_csv_data(data, filepath, delimeter=","):
    with open(filepath, "a", newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=delimeter)
        for data_item in data:
            csv_writer.writerow(data_item)