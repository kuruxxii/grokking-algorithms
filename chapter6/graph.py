# deque: list-like container with fast appends and pops on either end
from collections import deque

graph = {}
graph["you"] = ["claire", "alice", "bob"]
graph["claire"] = ["thom", "jonny"]
graph["alice"] = ["peggy"]
graph["bob"] = ["peggy", "anuj"]
graph["thom"] = []
graph["jonny"] = []
graph["peggy"] = []
graph["anuj"] = []


def is_seller(person):
    return person[-1] == 'm'


# BFS: breadth-first search
"""
广度优先搜索可回答两类问题：
- 从节点A出发，有前往节点B的路径吗
- 从节点A出发，前往节点B的哪条路径最短？
"""


def search(person):
    search_queue = deque()
    search_queue += graph[person]
    searched = []
    while search_queue:
        person_checking = search_queue.popleft()
        if not person_checking in searched:
            if is_seller(person_checking):
                print(f'{person_checking} is a seller')
                return True
            else:
                search_queue += graph[person_checking]
                searched.append(person_checking)
    print(f"There is no seller in {person}'s network")
    return False


search("you")
