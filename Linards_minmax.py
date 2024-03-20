from Linards_datu_struktura import generate_game_tree
import time
from math import inf
from functools import lru_cache


@lru_cache(10000)
def minimax(game_tree, level, node_id, depth, is_maximizing):
    if depth == 0 or not game_tree[level][node_id].children:
        if level % 2 != 0:
            return (game_tree[level][node_id].p2_points + game_tree[level][node_id].p2_rocks) - (
                    game_tree[level][node_id].p1_points + game_tree[level][node_id].p1_rocks), None
        else:
            return (game_tree[level][node_id].p1_points + game_tree[level][node_id].p1_rocks) - (
                    game_tree[level][node_id].p2_points + game_tree[level][node_id].p2_rocks), None
    if is_maximizing:
        max_eval = -inf
        for node_id2 in game_tree[level][node_id].children:
            score_eval = minimax(game_tree, level + 1, node_id2, depth - 1, False)[0]
            if score_eval > max_eval:
                ai_move = game_tree[level + 1][node_id2]
                max_eval = score_eval
        return max_eval, ai_move
    else:
        min_eval = inf
        for node_id2 in game_tree[level][node_id].children:
            score_eval = minimax(game_tree, level + 1, node_id2, depth - 1, True)[0]
            if score_eval < min_eval:
                ai_move = game_tree[level + 1][node_id2]
                min_eval = score_eval
        return min_eval, ai_move


def main():
    akmeni = 70
    game_tree_start = generate_game_tree(akmeni)
    max_depth = 50
    levels = 0
    start = time.time()
    print(game_tree_start[0][0])
    rock_buffer = game_tree_start[0][0].rocks
    move = game_tree_start[0][0]
    print("P1 takes", rock_buffer - move.rocks, " and moves =")
    print(move)
    Used_moves = []

    while 1:
        if not move.children:
            break
        rock_buffer = move.rocks
        move = minimax(game_tree_start, levels, move.node_id, max_depth, True)[1]
        if levels % 2 == 0:
            print("P1 takes", rock_buffer - move.rocks, " and moves =")
        else:
            print("P2 takes", rock_buffer - move.rocks, "and moves =")
        print(move)
        Used_moves.append(move)
        levels += 1

    print(move.p1_points + move.p1_rocks, move.p2_points + move.p2_rocks)
    print(len(Used_moves))
    end = time.time()
    print("___________________")
    print(end - start)


if __name__ == '__main__':
    main()
