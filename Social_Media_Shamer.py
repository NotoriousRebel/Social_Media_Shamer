import argparse
import tests

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-user', help="enter -user followed by username to test", type=str)
    parser.add_argument('-passw', help="enter -passw followed by password to test", type=str)
    args = parser.parse_args()
    output = []
    if args.user is not None:
        output.append(args.user)
    if args.passw is not None:
        output.append(args.passw)
    return output

def wrap_up(dict):
    for key in dict.keys():
        print(key, ': ', dict.get(key))

def main():
    output = parseArgs()
    username = output[0]
    password = output[1]
    dict = tests.call_tests(username, password)
    wrap_up(dict)

if __name__ == '__main__':
    main()
