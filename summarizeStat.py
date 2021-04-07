import sys
import csv
import os
import pandas as pd


def read_single_stat_file( file, config_name ):
    file1 = open(file, 'r')
    lines = file1.readlines()
    stat_dict = {'configuration': config_name}
    for line in lines:
        line = line.strip()
        if len(line) < 1:
            continue
        line_content = line.split()
        stat_dict[line_content[0]] = line_content[1]
    file1.close()
    return stat_dict

def read_file_line_by_line():
    file1 = open('targetStats', 'r')
    lines = file1.readlines()
    item_list = []
    for line in lines:
        item_list.append(line.strip())
    file1.close()
    return item_list

def write_to_csv(file, data_dict):
    with open(file, 'w') as output:
        writer = csv.writer(output)
        for key, value in data_dict.items():
            writer.writerow([key, value])

def filter_out_stats(original_dict):
    target_stats = read_file_line_by_line()
    target_stats.append('configuration')
    filtered_dict = {k: v for (k, v) in original_dict.items() if k in target_stats}
    return filtered_dict

def list_all_sub_directories(directory):
    return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]


input_directory = sys.argv[1]
output_file = sys.argv[2]

configurations = list_all_sub_directories(input_directory)

df = pd.DataFrame()
for configuration in configurations:
    stats = filter_out_stats(read_single_stat_file(input_directory + '/' + configuration + '/stats.txt', configuration))
    df = df.append(stats, ignore_index=True)

df.to_csv(output_file, index=False )