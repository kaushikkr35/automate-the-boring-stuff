def list_to_str(list_name):
    for i in range(len(list_name)):
        if i < len(list_name) - 1: 
            print(list_name[i] + ',', end = " ")
        else:
            print('and ' + list_name[i], end = " ")

user_list = []
user_input = input("Enter your list elements separated by space: ")
user_list = user_input.split()
list_to_str(user_list)
