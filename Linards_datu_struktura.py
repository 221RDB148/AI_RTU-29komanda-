node_counter = 0
is_end = True


class Variables:
    def __init__(self, node_id, parents, p1_points, p1_rocks, p2_points, p2_rocks, rocks):
        self.node_id = node_id
        self.parents = [parents]
        self.children = []
        self.p1_points = p1_points
        self.p1_rocks = p1_rocks
        self.p2_points = p2_points
        self.p2_rocks = p2_rocks
        self.rocks = rocks

    def __str__(self):
        return f"id:{self.node_id} {self.parents} {self.children} {self.p1_points} {self.p1_rocks} {self.p2_points} {self.p2_rocks} {self.rocks}"


def check_connections(node_id, p1_points, p1_rocks, p2_points, p2_rocks, rocks, x):
    #   Funkcija, kas salīdzina padotā objekta vērtības ar visām pēdējā līmeņa eksistējošajām objektu vērtībām,
    #   un ja tās ir vienādas, tad tiek pierakstīti vecāki un node bērni
    global node_counter

    for xxx in levels[-1]:
        if xxx.p1_points == p1_points and xxx.p1_rocks == p1_rocks and xxx.p2_points == p2_points and xxx.p2_rocks == p2_rocks and xxx.rocks == rocks:
            xxx.parents.append(node_id)
            x.children.append(xxx.node_id)
            return

    node_counter += 1
    levels[-1].append(Variables(node_counter, node_id, p1_points, p1_rocks, p2_points, p2_rocks, rocks))
    x.children.append(node_counter)


def create_level(current_level_list, current_level):
    global node_counter
    global is_end
    # if not current_level_list pārbauda vai pēdējais padotais lists ir tukšs, un ja tas ir, tad iziet no funkcijas un ar
    # is_end tiek pārtraukts cikls, kas callo šo funkciju
    if not current_level_list:
        is_end = False
        return
    #Tiek pievienots tukšš lists pie levels
    levels.append([])
    #Tiek iets cauri listam, kas satur objektus, kas ir x
    for x in current_level_list:
        if x.rocks - 2 >= 0:
            if (x.rocks - 2) % 2 == 0:
                if current_level % 2 == 0:
                    check_connections(x.node_id, x.p1_points + 2, x.p1_rocks + 2, x.p2_points, x.p2_rocks, x.rocks - 2, x)
                else:
                    check_connections(x.node_id, x.p1_points + 2, x.p1_rocks, x.p2_points, x.p2_rocks + 2, x.rocks - 2, x)
            else:
                if current_level % 2 == 0:
                    check_connections(x.node_id, x.p1_points, x.p1_rocks + 2, x.p2_points + 2, x.p2_rocks, x.rocks - 2, x)
                else:
                    check_connections(x.node_id, x.p1_points, x.p1_rocks, x.p2_points + 2, x.p2_rocks + 2, x.rocks - 2, x)
        if x.rocks - 3 >= 0:
            if (x.rocks - 3) % 2 == 0:
                if current_level % 2 == 0:
                    check_connections(x.node_id, x.p1_points + 2, x.p1_rocks + 3, x.p2_points, x.p2_rocks, x.rocks - 3, x)
                else:
                    check_connections(x.node_id, x.p1_points + 2, x.p1_rocks, x.p2_points, x.p2_rocks + 3, x.rocks - 3, x)
            else:
                if current_level % 2 == 0:
                    check_connections(x.node_id, x.p1_points, x.p1_rocks + 3, x.p2_points + 2, x.p2_rocks, x.rocks - 3, x)
                else:
                    check_connections(x.node_id, x.p1_points, x.p1_rocks, x.p2_points + 2, x.p2_rocks + 3, x.rocks - 3, x)


number = 12
id0 = Variables(0, None, 0, 0, 0, 0, number)
levels = [[id0]]
i = 0
while True:
    if not is_end:
        print("End")
        break
    create_level(levels[-1], i)
    i += 1
for xx in range(len(levels)):
    print("Level = " + str(xx))
    for jj in levels[xx]:
        print(jj)
