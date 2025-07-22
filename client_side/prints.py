from client_side.static import get_files_in_folder


def print_main_menu():
    print("""select the option:
    \t1.train and classify
    \t2. exit""")
def print_select_data():
    data_files = get_files_in_folder(r'../Naive_Bayes/data')
    print('select the data to train the model:')
    for i in range(len(data_files)):
        print(f'\t{i+1}. {data_files[i]}')

def print_select_target_column(columns):
    print(f'''select the the target column:''')
    for i in range(len(columns)):
        print(f'{columns[i]}', sep=', ')
    print('\npress Enter if the target class is the last column.')


def print_select_new_df():
    print('''select an option:
    1. select a new dataframe
    2. stay with the same dataframe''')

def print_select_index_column(columns):
    print(f'''select the index column:''')
    for i in range(len(columns)):
        print(f'{columns[i]}', sep=', ')
