'''
Miscellaneous utility functions
'''
import collections
import operator
import os
import time
import datetime
import shutil

def order_dictionary(dictionary, mode, reverse=False):
    # Tạo ra một dict mới từ original dict và dict mới được sắp xếp theo mode được truyền vào
    '''
    reverse: True: giảm dần, False: tăng dần
    mode: sort theo thứ tự nào, key_value: sort key xong đến value
    Order a dictionary by 'key' or 'value'.
    mode should be either 'key' or 'value'
    http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    '''

    if mode =='key':
        return collections.OrderedDict(sorted(dictionary.items(),
                                              key=operator.itemgetter(0),
                                              reverse=reverse))
    elif mode =='value':
        return collections.OrderedDict(sorted(dictionary.items(),
                                              key=operator.itemgetter(1),
                                              reverse=reverse))
    elif mode =='key_value':
        return collections.OrderedDict(sorted(dictionary.items(),
                                              reverse=reverse))
    elif mode =='value_key':
        return collections.OrderedDict(sorted(dictionary.items(),
                                              key=lambda x: (x[1], x[0]),
                                              reverse=reverse))
    else:
        raise ValueError("Unknown mode. Should be 'key' or 'value'")

def reverse_dictionary(dictionary):
    # Reverse giá trị cặp key-value trong dict.
    # Xử lý theo từng trường hợp là original dict hay dict đã được tạo từ original dict.
    '''
    http://stackoverflow.com/questions/483666/python-reverse-inverse-a-mapping
    http://stackoverflow.com/questions/25480089/right-way-to-initialize-an-ordereddict-using-its-constructor-such-that-it-retain
    '''
    #print('type(dictionary): {0}'.format(type(dictionary)))
    if type(dictionary) is collections.OrderedDict:
        #print(type(dictionary))
        return collections.OrderedDict([(v, k) for k, v in dictionary.items()])
    else:
        return {v: k for k, v in dictionary.items()}

def merge_dictionaries(*dict_args):
    # Merge các dict với nhau vào một dict mới, ưu tiên các giá trị trong các dict sau
    '''
    http://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-in-a-single-expression
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def pad_list(old_list, padding_size, padding_value):
    # Xử lý padding cho list với padding_size và padding_value được truyền vào
    '''
    http://stackoverflow.com/questions/3438756/some-built-in-to-pad-a-list-in-python
    Example: pad_list([6,2,3], 5, 0) returns [6,2,3,0,0]
    '''
    assert padding_size >= len(old_list)
    return old_list + [padding_value] * (padding_size-len(old_list))

def get_basename_without_extension(filepath):
    # Lấy tên file (không bao gồm extension)
    '''
    Getting the basename of the filepath without the extension
    E.g. 'data/formatted/movie_reviews.pickle' -> 'movie_reviews'
    '''
    return os.path.basename(os.path.splitext(filepath)[0])

def create_folder_if_not_exists(directory):
    # Tạo folder nếu nó không tồn tại
    '''
    Create the folder if it doesn't exist already.
    '''
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_current_milliseconds():
    # Tính thời gian theo milliseconds
    '''
    http://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
    '''
    return(int(round(time.time() * 1000)))

def get_current_time_in_seconds():
    # Lấy thời gian hiện tại theo format
    '''
    http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
    '''
    return(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))

def get_current_time_in_miliseconds():
    # Lấy thời gian hiện tại theo format đến miliseconds
    '''
    http://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
    '''
    return(get_current_time_in_seconds() + '-' + str(datetime.datetime.now().microsecond))

def convert_configparser_to_dictionary(config):
    # Convert từ configparser --> dict
    '''
    http://stackoverflow.com/questions/1773793/convert-configparser-items-to-dictionary
    '''
    my_config_parser_dict = {s:dict(config.items(s)) for s in config.sections()}
    return my_config_parser_dict

def get_parameter_to_section_of_configparser(config):
    # Get các parameter cho quá trình configparser
    parameter_to_section = {}
    for s in config.sections():
        for p, _ in config.items(s):
            parameter_to_section[p] = s
    return parameter_to_section

def copytree(src, dst, symlinks=False, ignore=None):
    # Copy toàn bộ các nội dung trong src vào dst (tồn tại)
    '''
    http://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
    '''
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
