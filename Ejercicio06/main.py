#Generar las intancias para cada mob
from mob import Mob
from creeper import Creeper    
from enderman import Enderman
from vaca import Vaca
from zombie import Zombie
 
if __name__ == "__main__":
    mobs = [
        Vaca("Bessie", 10),
        Creeper("Explosi", 20),
        Enderman("Tall Boi", 40),
        Zombie ("Zombie", 15),
    ]
    for mob in mobs:
        mob.presentarse()