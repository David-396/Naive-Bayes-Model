import os
from types import new_class


def get_max_classify_from_csv(class_dict):
    cls_lst = []
    for num,dic in class_dict.items():
        cls_lst.append(max(dic, key=dic.get))
    return cls_lst

def get_max_classify_from_record(class_dict):
    return max(class_dict, key=class_dict.get)

def split_df_by_precent(dataframe, precent : (float, int), from_bottom=False):
    if not from_bottom:
        n = round(len(dataframe)*precent)
        return dataframe.iloc[:n]
    n = -round(len(dataframe)*precent)
    return dataframe.iloc[n:]

def get_files_in_folder(folder_path):
    return os.listdir(folder_path)

def dict_to_str(dic):
    str_dic = {}
    for k,v in dic.items():
        str_dic[str(k)] = str(v)
    return str_dic