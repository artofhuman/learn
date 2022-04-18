from collections import deque

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["thom"] = []
graph["jonny"] = []
graph["peggy"] = []
graph["anuj"] = []


def is_seller(name):
    return name[-1] == "m"


def find_seller():
    search_queue = deque()
    search_queue += graph["you"]

    visited = []

    while search_queue:
        person = search_queue.popleft()

        if not person in visited:
            if is_seller(person):
                return person
            else:
                search_queue += graph[person]
                visited.append(person)

result = find_seller()

print(result)
