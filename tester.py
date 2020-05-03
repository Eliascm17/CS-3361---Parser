from pathlib import Path


def getTestCases():
    path = Path.cwd()
    testCases = path / 'testCases'
    # print(testCases)
    testInstances = []

    files = [e for e in testCases.iterdir() if e.is_file()]
    # print(files)

    # putting each line of each .txt file into a 2-D array
    for file in files:
        newTestCase = []
        with open(file) as f:
            for i, line in enumerate(f):
                # print ("{0}: {1}".format(i+1,line))
                newTestCase.append(line)

        testInstances.append(newTestCase)

    # for some reason '\n' is being appended to each string when added to the newTestCase array
    for i in range(len(testInstances)):
        for j in range(len(testInstances[i])):
            if "\n" in testInstances[i][j]:
                length = len(testInstances[i][j])
                testInstances[i][j] = testInstances[i][j][:length-1]

    return testInstances
