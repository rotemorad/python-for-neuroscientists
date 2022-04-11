from collections import namedtuple
from enum import Enum

Type = Enum("Type", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def get_available_agents(agents: tuple):
    """
        Eliminates dead and healthy agents, since the healthy ones don'nt leave their house and the dead are well... dead.

        Parameters
        ----------
        agents : tuple

        Returns
        -------
        available_agents : list
            The agents available to meet other agents- they are not HEALTHY nor DEAD.
        non_available_agents: list
            The agents who are not going to meet other agents- they are HEALTHY or DEAD.
        """

    available_agents = list(filter(lambda agent: agent.category not in (Type.HEALTHY, Type.DEAD), agents))
    non_available_agents = list(filter(lambda agent: agent.category in (Type.HEALTHY, Type.DEAD), agents))
    return available_agents, non_available_agents


def pair_agents(available_agents: list):
    """
        Pairs agents according to their index in the available agents list, so agent[0] will pair with agent[1] and so.
        If there's an uneven number of agents- return the last agent.

        Parameters
        ----------
        available_agents : list
            The agents available to meet other agents- they are not HEALTHY nor DEAD.

        Returns
        -------
        pairs: list
            List of paired agents. The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...)
        last_agent: Agent or None
        """

    if len(available_agents) % 2 == 0:
        even_agents = available_agents
        last_agent = None
    else:
        even_agents = available_agents[:-1]
        last_agent = available_agents[-1]

    pairs = []
    for i in range(0, len(even_agents), 2):
        pairs.append((even_agents[i:i + 2]))

    return pairs, last_agent


def change_category(agent: Agent, other_agent: Agent):
    """
    Get the updated agent after a meeting with other_agent.

    Parameters
    ----------
    agent : Agent
        The original agent. His category can be either CURE, SICK, or DYING.
    other_agent : Agent
        The other agent in the meeting.

    Returns
    -------
    updated_agent : Agent
        The updates agent.
    """

    # If agent is cure, there's nothing to do
    if agent.category is not Type.CURE:
        diff = -1 if other_agent.category is Type.CURE else 1
        updated_agent = Agent(agent.name, Type(agent.category.value + diff))
    else:
        updated_agent = agent

    return updated_agent


def meetup(agent_listing: tuple):
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Type.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """

    # split to agents available for meetings and the rest
    available_agents, non_available_agents = get_available_agents(agent_listing)

    # split to pairs, and the last agent
    pairs, last_agent = pair_agents(available_agents)

    updated_listing = []
    for agent_1, agent_2 in pairs:
        # get the updated agents
        new_agent_1 = change_category(agent_1, agent_2)
        new_agent_2 = change_category(agent_2, agent_1)

        # add the updates agents to the updates listing
        updated_listing += [new_agent_1, new_agent_2]

    # add the last agent if it exists
    if last_agent:
        updated_listing.append(last_agent)

    # insert all the agent that weren't in any meetings
    updated_listing += non_available_agents

    return updated_listing
