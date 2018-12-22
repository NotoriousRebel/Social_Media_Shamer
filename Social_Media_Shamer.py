import argparse
import tests

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help="enter -u followed by username to test", type=str)
    parser.add_argument('-p', help="enter -p followed by password to test", type=str)
    parser.add_argument('-f', help="enter -f followed by path to text file, formatted as username password",type=str)
    parser.add_argument('-ft',help="if using a file enter -ft to indicate you are",action="store_true") #store as boolean
    args = parser.parse_args() #get args
    output = []
    if args.u is not None:
        output.append(args.u)
    if args.p is not None:
        output.append(args.p)
    if args.f is not None:
        output.append(args.f)
    if args.ft:
        output.append('File_Exists') #string that indicates file exists
    return output

def handle_file(file_path):
    dict_list = [] #intialize list for dicts
    with open(file_path,'r') as file: #open file just to read
        credentials = file.read()
        for cred in credentials.strip().splitlines():
            cred = cred.split(' ') #split on empty space
            username = cred[0]
            password = cred[1]
            dict_list.append(tests.call_tests(username,password,file_flag=True)) #pass in file_flag and append dict
    return dict_list

def wrap_up(dictionary,file_flag=True):
    if file_flag: #if user passed in a file
        dictionary_list = dictionary
        for dictionary in dictionary_list: #iterate through dictionaries
            for key in dictionary.keys(): #then interate through keys in dicts to print out info
                print(key, ': ',dictionary.get(key))
    else:
        for key in dictionary.keys():
            print(key, ': ', dictionary.get(key))

def main():
    args = parseArgs() #get args
    if 'File_Exists' in args: #if file exists in args
           file_path = args[args.index('File_Exists')-1]#get filepath
           dict_list = handle_file(file_path)
           wrap_up(dict_list, file_flag=True)
    else:
       username = args[0]
       password = args[1]
       dictionary = tests.call_tests(username, password,file_flag=False)
       wrap_up(dictionary)

if __name__ == '__main__':
    main()
