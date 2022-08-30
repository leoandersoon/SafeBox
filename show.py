from sorcery import dict_of

def show_data(website, username, password):
    new_dict = dict_of(website, username, password)
    print(new_dict)