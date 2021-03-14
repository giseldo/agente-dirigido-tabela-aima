from Enviroment import Environment

import random

class TrivialVacuumEnvironment(Environment):
    """This environment has two locations, A and B. Each can be Dirty
    or Clean. The agent perceives its location and the location's
    status. This serves as an example of how to implement a simple
    Environment."""

    loc_A, loc_B = (0, 0), (1, 0)  # The two locations for the Vacuum world

    def __init__(self):
        super().__init__()
        self.status = {self.loc_A: random.choice(['Clean', 'Dirty']),
                       self.loc_B: random.choice(['Clean', 'Dirty'])}

    def thing_classes(self):
        #return [Wall, Dirt, ReflexVacuumAgent, RandomVacuumAgent, TableDrivenVacuumAgent, ModelBasedVacuumAgent]
        return []

    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Clean)."""
        return agent.location, self.status[agent.location]

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move."""
        if action == 'Right':
            agent.location = self.loc_B
            agent.performance -= 1
        elif action == 'Left':
            agent.location = self.loc_A
            agent.performance -= 1
        elif action == 'Suck':
            if self.status[agent.location] == 'Dirty':
                agent.performance += 10
            self.status[agent.location] = 'Clean'

    def default_location(self, thing):
        """Agents start in either location at random."""
        return random.choice([self.loc_A, self.loc_B])