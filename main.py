def main():
    file_path = "books/frankenstein.txt"
    contents = open_file(file_path)
    count =  word_count(contents)
    char_count = char_occurance_count(contents)
    orderd_count = dict_reorder(char_count)
    print_report(orderd_count, count, file_path)


def open_file(file_path : str):
    with open(file_path) as f:
        contents = f.read()
    return contents

def word_count(string : str):
    cnt = string.split()
    return len(cnt)

def char_occurance_count(string : str):
    char_occurance = {} 
    str = string.lower()
    for s in str:
        if s.isalpha():
            if s in char_occurance:
                char_occurance[s] += 1
            else: 
                char_occurance[s] = 1
    return char_occurance

def sort_on(dict):
    return dict['count']
    
def dict_reorder(char_occurance : dict):
    lst = []
    for v in char_occurance.items():
        pairs = {}
        pairs['letter'] = v[0]
        pairs['count'] = v[1]
        lst.append(pairs)
    lst.sort(reverse=True, key=sort_on)
    return lst 

def print_report(data : list, count : int, file_name : str):
    print(f"--- Begin report of {file_name} ---")
    print(f"{count} words found in the document\n")
    for x in data:
        print(f"The '{x['letter']}' character was found {x['count']} times")
    print("--- End report ---")

main()
