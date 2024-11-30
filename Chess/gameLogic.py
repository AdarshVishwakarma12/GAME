from env import *

def state_1(x, y, agent_run_black):
    if agent_run_black is True:
        for i in agent_black.instance:
            if i.pos[0] == x and i.pos[1] == y: return i
    elif agent_run_black is False:
        for i in agent_white.instance:
            if i.pos[0] == x and i.pos[1] == y: return i
    return None
def state_2(x, y, cool , hot, agent_run_black, lst = list()):
    for i in cool:
        if i[0] == x and i[1] == y: return True
    for i in hot:
        if i[0] == x and i[1] == y:
            for j, j1 in enumerate(enviornment.instance):
                if j1.pos == [x, y]: break
            if agent_run_black is False:
                for k, k1 in enumerate(agent_black.instance):
                    if j1 == k1: break
                del agent_black.instance[k]
            elif agent_run_black is True:
                for k, k1 in enumerate(agent_white.instance):
                    if j1 == k1: break
                del agent_white.instance[k]
            print('command report', enviornment.instance[j], 'is being kicked out')
            del enviornment.instance[j]
            return False
    return None
