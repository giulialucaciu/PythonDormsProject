from domain.domain import Dorms
from infrastructure.repo import Repo

# //function for printing te repository
def printRepo(repo):
    for application in repo.get_repo():
        print(application)


application1 = Dorms(1, "Giulia", "Economica 2")
application2 = Dorms(2, "Andrei", "Caminul 16")
application3 = Dorms(3, "Laurentiu", "Economica 1")

repo = Repo()

# add every application one by one into the repository
try:
    repo.add_repo(application1)
except Exception as ex:
    print("exception" + str(ex))

try:
    repo.add_repo(application2)
except Exception as ex:
    print("exception" + str(ex))

try:
    repo.add_repo(application3)
except Exception as ex:
    print("exception" + str(ex))


# print each function
print("---------")
print("function: add")
printRepo(repo)

print("---------")
print("function: greater than")
print(repo.greater_than(1))


print("---------")
print("function: sorted by name")
print(repo.sort_student())