from functions.table_index import table_index
from functions.action_table import action_table
from characters.batman import *
import characters.watchmen

print(f"{nightwing.name} tries to punch {deadshot.name}.")
print(f"The Acting Value is {nightwing.name}'s Dexterity, which is {nightwing.dext}.")
print(f"The Opposing Value is {deadshot.name}'s Dexterity, which is {deadshot.dext}.")
print(f"On the action table, we go to the {table_index(nightwing.dext)}th row and the {table_index(deadshot.dext)}th column.")
print(f"Action table result: {action_table(nightwing.dext,deadshot.dext)}.")

print(f"{characters.watchmen.nite_owl.name}'s Will is {characters.watchmen.nite_owl.will}.")