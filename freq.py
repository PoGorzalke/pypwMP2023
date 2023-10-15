def words_count(text: str) ->dict:
    text = text.lower()
    text = text.replace(",","").replace(".","")
    my_list = text.split()
    my_dict = dict.fromkeys(my_list, 0)
    for item in my_list:
        my_dict[item] += 1
    return my_dict


print(
    words_count("this This. this")
)







