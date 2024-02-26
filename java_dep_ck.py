import os


lst_classes = []
#tupl_classes = None
lst_files = []
#tupl_files = None
result = []


# def confirm_classes():
#     tupl_classes = tuple(lst_classes)
#     return tupl_classes

# def confirm_files():
#     tupl_files = tuple(lst_files)
#     return tupl_files

def find_files():#filename: str):
    file_list = os.listdir(os.getcwd())#os.curdir())# '경로')
    for lst in file_list:
        if lst[-5:] == ".java":
            lst_files.append(lst)
    # print(lst_files)

def find_classes(filename: str):
    lst = []
    #read = open(file=filename, mode="r") #, encoding="")
    #line = read.readline
    with open(filename, 'r') as file:
        #lines = file.readlines()
        #for line in lines:
        line = file.readline
        while line:
            words = str(line)
            words = words.replace("{", " ")
            words = words.split(" ")
            for wrd in words:
                if wrd == "class":
                    lst.append(words[words.index("class") + 1])
        line = read.readline
    print("5")
    lst_classes.append(lst)

def check_classes(filename: str):
    read = open(file=filename, mode="r") #, encoding="")
    line = read.readline
    while line:
        for clses in lst_classes:
            if lst_classes.index(clses) == lst_files.index(filename): continue
            for cls in clses:
                if (line.find(cls) != -1) and (filename + "<-" + lst_classes.index(clses) not in result):
                    result.append(filename + "<-" + lst_classes.index(clses))
        line = read.readline

def main():
    find_files()
    #confirm_files()
    for file in lst_files:
        find_classes(file)
    print("2")
    for file in lst_files:
        check_classes(file)
    print(result)

if __name__ == "__main__":
    main()
