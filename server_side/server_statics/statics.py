def get_max_classify_from_csv(class_dict):
    cls_lst = []
    for num,dic in class_dict.items():
        cls_lst.append(max(dic, key=dic.get))
    return cls_lst

def get_max_classify_from_record(class_dict):
    return max(class_dict, key=class_dict.get)
