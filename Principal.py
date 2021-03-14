from Agent import Agent
from Enviroment import Environment
from Thing import Thing
from TrivialVacuumEnvironment import TrivialVacuumEnvironment

def TableDrivenAgentProgram(table):
    percepts = []
    def program(percept):
        percepts.append(percept)
        action = table.get(tuple(percepts))
        return action
    return program

def TableDrivenVacuumAgent():
    loc_A, loc_B = (0, 0), (1, 0)  # The two locations for the Vacuum world
    table = {((loc_A, 'Clean'),): 'Right',
             ((loc_A, 'Dirty'),): 'Suck',
             ((loc_B, 'Clean'),): 'Left',
             ((loc_B, 'Dirty'),): 'Suck',
             ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
             ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
             ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
             ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
             ((loc_A, 'Dirty'), (loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
             ((loc_B, 'Dirty'), (loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck'}
    return Agent(TableDrivenAgentProgram(table))

agente = TableDrivenVacuumAgent()
ambiente = TrivialVacuumEnvironment()
ambiente.add_thing(agente)
ambiente.run()
print("Resultado : {}" .format(ambiente.status == {(1,0):'Clean' , (0,0) : 'Clean'}))

