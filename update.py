from git import Repo
from colored import fg

success = fg('green')
error = fg('red')
projects = ''

def main():
    getProjects()
    print(projects)
    gitPull('main')

def getProjects():
    f = open('projects.txt')
    global projects
    projects = f.read()
    f.close()
    projects = projects.split(",")

def gitPull(branch):
    for i in projects:
        print(i)
        print_s('Doing pulls on ' + i)
        repo = Repo(i)
        origin = repo.remotes.origin
        origin.pull()

def print_s(str):
    print(success + str)

def print_e(str):
    print(error + str)

main()
