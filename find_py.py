#
#   @author      : SRvSaha
#   Filename     : find_py.py
#   Timestamp    : 20:01 10-August-2016 (Wednesday)
#   Description  : Function that finds the python files from the list
#

def find_py(my_list):
    output = []
    for item in my_list:
        # if '.py' in item:
        if item.endswith('.py'):
            output.append(item)
    return output

#TESING
names = ['dist', 'MANIFEST.in', 'AUTHORS', '.gitignore', 'setup.py', '.travis.yml', 'README.rst', 'run.py', 'gpl.txt', '.coveragerc', '.git', 'LICENSE', 'appveyor.yml', 'tests', 'Makefile', 'requirements.txt', 'conf', 'mu.egg-info', 'mu', 'package', 'CONTRIBUTING.rst', 'docs']
print(find_py(names))
