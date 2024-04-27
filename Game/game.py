from typing import List, Tuple, Callable
from random import randint, shuffle


Playground = List[List[bool]] # Definujeme typ Playground, což bude vždy pole polí boolů

def print_state(playground: Playground) -> None:
    """
    Vypíše herní plán
    """
    for i in playground:
        for j in i:
            if j == False:
                print(".", end="")
            if j == True:
                print("#", end="")
        print()        
                

def is_full(playground: Playground) -> bool:
    """
    Vrátí True, pokud je plán celý zaplněný
    """
    for i in playground:
        for j in i:
            if j == False:
                return False
    return True


def get_turn_player(playground: Playground) -> Tuple[int, int]:
    """
    Načte od uživatele pole, kam chce hrát a vrátí jeho souřasnice
    """
    playground_height = len(playground)
    playground_width = len(playground[0])
    print("Zadej políčko (řádek mezera sloupec):")
    coords = tuple(input("").split())
    y = coords[0]
    x = coords[1]
    while int(y) > playground_height or int(y) < 0 or int(x) > playground_width or int(x) < 0 or playground[int(y)][int(x)] == True:
        print("Neplatné souřadnice, zkus to znovu")
        print("Zadej políčko (řádek mezera sloupec):")
        coords = tuple(input("").split())
        y = coords[0]
        x = coords[1]
    return (str(y), str(x))
        
    
def strategy_iterative(playground: Playground) -> Tuple[int, int]:
    """
    Postupná strategie. Vrátí souřadnice, na která se má hrát.
    """
    for i in range(len(playground)):
        for j in range(len(playground[0])):
            if playground[i][j] == False:
                print(i, j)
                return (str(i), str(j))


def strategy_random(playground: Playground) -> Tuple[int, int]:
    """
    Náhodná strategie. Vrátí souřadnice, na která se má hrát.
    """
    playground_height = len(playground)
    playground_width = len(playground[0])
    while True:
        y = randint(0, playground_height)
        x = randint(0, playground_width)
        if playground[y][x] == False:
            return (str(y), str(x))


def strategy_max_block(playground: Playground) -> Tuple[int, int]:
    """
    Maximálně blokující strategie. Vrátí souřadnice, na která se má hrát.
    """
    z = 5
    playground_height = len(playground)
    playground_width = len(playground[0])
    for _ in range(5):
        for y in range(len(playground)):
            for x in range(len(playground[0])):
                h = 0
                if playground[int(y)][int(x)] == False:
                    h += 1
                if int(y)+1 < playground_height:
                    if playground[int(y)+1][int(x)] == False:
                        h += 1
                if int(y)-1 >= 0:
                    if playground[int(y)-1][int(x)] == False:
                        h += 1
                if int(x)+1 < playground_width:
                    if playground[int(y)][int(x)+1] == False:
                        h += 1
                if int(x)-1 >= 0:
                    if playground[int(y)][int(x)-1] == False:
                        h += 1
                if h == (z-_):
                    return (str(y), str(x))


def strategy_min_block(playground: Playground) -> Tuple[int, int]:
    
    """
    Minimálně blokující strategie. Vrátí souřadnice, na která se má hrát.
    """
    playground_height = len(playground)
    playground_width = len(playground[0])
    for _ in range(4):
        for y in range(len(playground)):
            for x in range(len(playground[0])):
                h = 0
                if playground[int(y)][int(x)] == False:
                    h += 1
                if int(y)+1 < playground_height:
                    if playground[int(y)+1][int(x)] == False:
                        h += 1
                if int(y)-1 >= 0:
                    if playground[int(y)-1][int(x)] == False:
                        h += 1
                if int(x)+1 < playground_width:
                    if playground[int(y)][int(x)+1] == False:
                        h += 1
                if int(x)-1 >= 0:
                    if playground[int(y)][int(x)-1] == False:
                        h += 1
                if h == _+1:
                    return (str(y), str(x))


def strategy_ending(playground: Playground) -> Tuple[int, int]:
    """
    Inteligentní zakončovač. Vrátí souřadnice, na která se má hrát.
    """
    z = 0
    playground_height = len(playground)
    playground_width = len(playground[0])
    for i in range(len(playground)):
        for j in range(len(playground[0])):
            if j == False:
                z += 1
    if z <= 5:
        for y in range(len(playground)):
            for x in range(len(playground[0])):
                x = 0
                if playground[int(y)][int(x)] == False:
                    x += 1
                if int(y)+1 < playground_height:
                    if playground[int(y)+1][int(x)] == False:
                        x += 1
                if int(y)-1 >= 0:
                    if playground[int(y)-1][int(x)] == False:
                        x += 1
                if int(x)+1 < playground_width:
                    if playground[int(y)][int(x)+1] == False:
                        x += 1
                if int(x)-1 >= 0:
                    if playground[int(y)][int(x)-1] == False:
                        x += 1
                if x == z:
                    return (str(y), str(x))
    else:
        return(strategy_random(playground))
        

def game_options():
    print("Vyberte hráče:")
    print("1: Uživatel")
    print("2: Postupná strategie")
    print("3: Náhodná strategie")
    print("4: Maximálně blokující strategie")
    print("5: Minimálně blokující strategie")
    print("6: Inteligentní zakončovač")
def game_interface() -> None:
    """
    Načte od uživatele, jaké mají být rozměry pole kdo proti komu bude hrát, a poté odehraje jednu hru.
    """
    playground = []
    print("Zadejte výšku plánu:", end="")
    playground_height = int(input())
    for i in range(playground_height):
        playground.append([])
    print("Zadejte šířku plánu:", end="")
    playground_width = int(input())
    for j in range(playground_width):       # vygeneruje pole
        for i in playground:
            i.append(False)
    print("Kdo bude hrát jako první?")
    game_options()
    player = []
    player.append(int(input()))             # výběr hráče
    if player[0] < 1 or player[0] > 6:
        print("Špatná volba!")
        return()
    game_options()
    player.append(int(input()))             # výběr druhého hráče
    if player[1] < 1 or player[1] > 6:
        print("Špatná volba!")
        return()
    while is_full(playground) == False:
        turn = 1
        playground_height = len(playground)
        playground_width = len(playground[0])
        while is_full(playground) == False:
            if turn % 2 == 0:
                hráč = 2
            else:
                hráč = 1
            print_state(playground)
            print("Tah " + str(turn) + ", hraje hráč " + str(hráč) + ":")
            if player[hráč - 1] == 1:
                tuple1 = get_turn_player(playground)
            elif player[hráč - 1] == 2:
                tuple1 = strategy_iterative(playground)
            elif player[hráč - 1] == 3:
                tuple1 = strategy_random(playground)
            elif player[hráč - 1] == 4:
                tuple1 = strategy_max_block(playground)
            elif player[hráč - 1] == 5:
                tuple1 = strategy_min_block(playground)
            elif player[hráč - 1] == 6:
                tuple1 = strategy_ending(playground)
            
            y = tuple1[0]
            x = tuple1[1]
            playground[int(y)][int(x)] = True
            if int(y)+1 < playground_height:
                playground[int(y)+1][int(x)] = True
            if int(y)-1 >= 0:
                playground[int(y)-1][int(x)] = True
            if int(x)+1 < playground_width:
                playground[int(y)][int(x)+1] = True
            if int(x)-1 >= 0:
                playground[int(y)][int(x)-1] = True
            turn += 1
    print_state(playground)
    print("Vyhrál hráč " + str(hráč))
            
game_interface()

#Známé nedostatky: Veškeré taktiky by měly fungovat bez problémů (minimálně když jsou použity proti hráči), o nějakých větších nedostatcích momentálně nevím.
#Styl: Pravděpodobně by se některé části kódu daly shrnout do samostatných funkcí, ale v rámci funkčnosti to ponechávám raději takto.