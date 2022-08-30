from git import Repo

def main():
    f = open('projects.txt')
    help = f.read()
    f.close()
    print(help)
    help = help.split(",")
    print(help)
    # Repo.git.pull
    repo = Repo('/Users/tylerpranger/Documents/htdocs/update_projects')
    origin = repo.remotes.origin
    origin.pull()
    # repo.git.pull
    # repo.git.checkout('main')
    # repo.git.commit('testing commit')
    print('hello 1')


main()
