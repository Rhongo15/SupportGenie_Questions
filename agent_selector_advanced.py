import random
import time

""" 
The function takes a list of dictionaries containing each agent's details, a selection mode and a list of issues as arguments
and returns a dictionary that contains every issue's index number as key and a list of possible agents for that issue as the 
key's value.

Index of issue values was used to allow for duplicacy of issues. The issues list can have multiple instances of 'Sales' and 
using index helps seperate such multiple instances of 'Sales'. 

A for loop is used to iterate through each issue and the agents with that issue in their roles are first selected and added
to possible_agents list.

Then based on the selection mode, the final list of agents are decided.

For all available, all agents in possible_agents list with 'is_available' set to True are added to present_to list.

For random, all agents that satisfy the critieria are collected and an agent is chosen at random using the random function.

For least busy, the agent is selcted based on the agents 'available_since' value. The strptime function was used to convert
'available_since' values in datetime objects and min() was applied to find the least busy agent.

The function returns the index of the selected agents. Since a ID function was not specified for agents, index was used to
identify them.  
"""

def agent_selector(agents, selection_mode, issues):
    issue_agent = {}
    for value in range(len(issues)):
        issue = issues[value]
        possible_agents = []
        #identifying agents with the issue in their roles list
        for agent in agents:
            if issue in agent['Roles']:
                possible_agents.append(agent)
        present_to = [] 
        #Selecting all available agents
        if selection_mode == "all available":
            for agent in possible_agents:
                if agent['is_available'] == True:
                    index = agents.index(agent)
                    present_to.append(index)
        #identifying all available agents and randomly selecting one agent from that       
        elif selection_mode == "random":
            random_c = []
            for agent in possible_agents:
                if agent['is_available'] == True:
                    index = agents.index(agent)
                    random_c.append(index)
            if not random_c:
                pass;
            else:
                present_to.append(random.choice(random_c))
        #converting available_since values into datetime format and applying min() gives the least busy agent
        else:
            agent_time = {}
            format = '%m/%d/%Y %I:%M %p'
            for agent in possible_agents:
                if agent['is_available'] == True:
                    x = time.strptime(agent['available_since'], format)
                    index = agents.index(agent)
                    agent_time[index] = x  #agent time is a dict that contains agent index and available since values
            for i in agent_time:
                if agent_time[i] == min(agent_time.values()):   #applying min() to agent_time.values() gives least busy time. Corresponding agent is identified using the key value
                    present_to.append(i)
        issue_agent[value] = present_to  #issue_agent is a dict containing issue index as key and possible agent list as value
    return issue_agent;