# return the max class value by his precent - classified from csv file
def get_max_classify_from_csv(class_dict):
    cls_lst = []
    for num,dic in class_dict.items():
        cls_lst.append(max(dic, key=dic.get))
    return cls_lst

# return the max class value by his precent - classified from record
def get_max_classify_from_record(class_dict):
    return max(class_dict, key=class_dict.get)

# splitting the dataframe by precent input
def split_df_by_precent(dataframe, precent : (float, int), from_bottom=False):
    if not from_bottom:
        n = round(len(dataframe)*precent)
        return dataframe.iloc[:n]
    n = -round(len(dataframe)*precent)
    return dataframe.iloc[n:]

# converting the dictionary types to string
def dict_to_str(dic):
    str_dic = {}
    for k,v in dic.items():
        str_dic[str(k)] = str(v)
    return str_dic
