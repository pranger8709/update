def main():
    f = open('projects.txt')
    help = f.read()
    f.close()
    print(help)
    help = help.split(",")
    print(help)


main()