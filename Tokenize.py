import json
from bs4 import BeautifulSoup


def read_bookkeeping_json():
    with open("/Users/Jamshir-MAC/Documents/Everything UC Irvine/Winter 2018/INF 241 Information Retrieval/Project/Project_3_Search_Engine/WEBPAGES_CLEAN/bookkeeping.json","r") as filehandle:
        j = json.load(filehandle)
        return j
        filehandle.close()


def tokenize(file_contents):
    index = file_contents.find("<body>")
    if(index != -1):
        title = file_contents[:index].strip()
        print(title)
        file_contents = file_contents[index:]
    
    soup = BeautifulSoup(file_contents, 'lxml')


def read_file(file_path):
    with open("/Users/Jamshir-MAC/Documents/Everything UC Irvine/Winter 2018/INF 241 Information Retrieval/Project/Project_3_Search_Engine/WEBPAGES_CLEAN/" + file_path,"r") as filehandle:
        file_contents = filehandle.read()
        tokenize(file_contents)
        filehandle.close()

if __name__ == '__main__':
    parsed_json = read_bookkeeping_json()
    
    for k,v in parsed_json.items():
        #TODO check if v (i.e. the URL is valid)
        #read_file(k)
        read_file("68/0")
        break
