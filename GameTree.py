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

    # Nomaina kā tiek izvadīts print(object), mainās tikai vizuāli
    def __str__(self):
        return f"id:{self.node_id} {self.parents} {self.children} {self.p1_points} {self.p1_rocks} {self.p2_points} {self.p2_rocks} {self.rocks}"


def generate_game_tree(rock_n):
    def check_connections(node_id, p1_points, p1_rocks, p2_points, p2_rocks, rocks, current_level):
        #   Funkcija, kas salīdzina padotā objekta vērtības ar visām pēdējā līmeņa eksistējošajām objektu vērtībām,
        #   un ja tās ir vienādas, tad tiek pierakstīti vecāki un node bērni
        nonlocal node_counter

        for latest_level in levels[-1]:
            if (latest_level.p1_points == p1_points and latest_level.p1_rocks == p1_rocks and
                    latest_level.p2_points == p2_points and latest_level.p2_rocks == p2_rocks and
                    latest_level.rocks == rocks):
                latest_level.parents.append(node_id)
                current_level.children.append(latest_level.node_id)
                return

        levels[-1].append(Variables(node_counter, node_id, p1_points, p1_rocks, p2_points, p2_rocks, rocks))
        current_level.children.append(node_counter)
        node_counter += 1

    def create_level(current_level_list, current_level) -> None:
        nonlocal node_counter
        node_counter = 0
        nonlocal is_end
        nonlocal levels
        # if not current_level_list pārbauda vai pēdējais padotais lists ir tukšs, un ja tas ir, tad iziet no funkcijas
        # un ar is_end tiek pārtraukts cikls, kas callo šo funkciju
        if not current_level_list:
            is_end = True
            return
        # Tiek pievienots tukšs lists pie levels
        levels.append([])
        # Tiek iets cauri listam, kas satur objektus, kas ir x un veikti visi iespējamie atļautie gājieni
        for x in current_level_list:
            if x.rocks - 2 >= 0:
                if (x.rocks - 2) % 2 == 0:
                    if current_level % 2 == 0:
                        check_connections(x.node_id, x.p1_points + 2, x.p1_rocks, x.p2_points, x.p2_rocks + 2,
                                          x.rocks - 2, x)
                    else:
                        check_connections(x.node_id, x.p1_points, x.p1_rocks + 2, x.p2_points + 2, x.p2_rocks,
                                          x.rocks - 2, x)
                else:
                    if current_level % 2 == 0:
                        check_connections(x.node_id, x.p1_points, x.p1_rocks, x.p2_points + 2, x.p2_rocks + 2,
                                          x.rocks - 2, x)
                    else:
                        check_connections(x.node_id, x.p1_points + 2, x.p1_rocks + 2, x.p2_points, x.p2_rocks,
                                          x.rocks - 2, x)
            if x.rocks - 3 >= 0:
                if (x.rocks - 3) % 2 == 0:
                    if current_level % 2 == 0:
                        check_connections(x.node_id, x.p1_points + 2, x.p1_rocks, x.p2_points, x.p2_rocks + 3,
                                          x.rocks - 3, x)
                    else:
                        check_connections(x.node_id, x.p1_points, x.p1_rocks + 3, x.p2_points + 2, x.p2_rocks,
                                          x.rocks - 3, x)
                else:
                    if current_level % 2 == 0:
                        check_connections(x.node_id, x.p1_points, x.p1_rocks, x.p2_points + 2, x.p2_rocks + 3,
                                          x.rocks - 3, x)
                    else:
                        check_connections(x.node_id, x.p1_points + 2, x.p1_rocks + 3, x.p2_points, x.p2_rocks,
                                          x.rocks - 3, x)

    node_counter = 0
    is_end = False

    # Tiek izveidots pirmais sākuma elements, no kura tiks ģenerēti pārējie gājieni
    levels = [[Variables(0, None, 0, 0, 0, 0, rock_n)]]
    i = 1

    # Cikls, kas veidi datu struktūru līmeni pa līmenim, līdz pēdējais lists ir tukšs, tad tas beidz darbu
    while True:
        if is_end:
            print("End")
            break
        create_level(levels[-1], i)
        i += 1

    # Pārvērš beigās iegūto list of list par tuple of tuples
    return tuple(tuple(x) for x in levels)


def print_nodes(levels) -> None:
    for level in range(len(levels)):
        print("Level = " + str(level))
        for node in levels[level]:
            print(node)


def main() -> None:  # Testēšanai
    n = int(input("Ar cik akmeņiem ģenerēt koku: "))
    game_tree = generate_game_tree(n)
    print_nodes(game_tree)

    # Piekļūt jebkuram elementam iespējams ar game_tree[x][y]
    # Kur x ir līmenis un y ir objekta indekss(0-...)


if __name__ == '__main__':
    main()
