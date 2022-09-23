from champ import Summoner
from blade import Blade

shuriken = Blade("shuriken",90)
kunai = Blade("kunai",75)

summoner1 = Summoner("Zed",800,85,shuriken)
summoner2 = Summoner("Yasuo",780,75,"None")

print(shuriken.get_name(),"|",shuriken.get_damage_amount())

print(summoner1.get_pseudo())

print(summoner1.get_weapon().get_name())
summoner2.set_weapon(kunai)
print(summoner2.get_weapon().get_damage_amount())

"""summoner1.attack_player(summoner2)

print(summoner1.get_pseudo(), "attaque", summoner2.get_pseudo())
print(summoner1.get_pseudo(),"|",summoner1.get_health())
print(summoner2.get_pseudo(),"|",summoner2.get_health())"""