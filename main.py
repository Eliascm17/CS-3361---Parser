from pprint import pprint
from Parser import Parser
import tester

def main():
    testCases = tester.getTestCases()
    pprint(testCases)
    print('\n')

    for i in range(len(testCases)):
        print('Batch {0}: {1}'.format(i+1, testCases[i]))
        try:
            p = Parser(testCases[i])
            p.parse()
        except:
            print('Error')

if __name__ == '__main__':
    main()
