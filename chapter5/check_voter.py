voted = {}


def check_vote(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote")


check_vote("Tom")
check_vote("Phil")
check_vote("Tom")
