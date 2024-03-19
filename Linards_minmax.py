from Linards_datu_struktura import generate_game_tree

akmeni = 17

game_tree_start = generate_game_tree(akmeni)


def minimax(game_tree, level, node_id, depth, is_maximizing):
    ai_move = None
    if depth == 0 or not game_tree[level][node_id].children:
        return (game_tree[level][node_id].p1_points + game_tree[level][node_id].p1_rocks) - (game_tree[level][node_id].p2_points + game_tree[level][node_id].p2_rocks), ai_move
    if is_maximizing:
        max_eval = -float('inf')
        for node_id2 in game_tree[level][node_id].children:
            score_eval = minimax(game_tree, level + 1, node_id2, depth - 1, False)[0]
            if score_eval > max_eval:
                ai_move = game_tree[level + 1][node_id2]
                max_eval = score_eval
        return max_eval, ai_move
    else:
        min_eval = float('inf')
        for node_id2 in game_tree[level][node_id].children:
            score_eval = minimax(game_tree, level + 1, node_id2, depth - 1, True)[0]
            if score_eval < min_eval:
                ai_move = game_tree[level + 1][node_id2]
                min_eval = score_eval
        return min_eval, ai_move


max_depth = 15
levels = 1
#print(game_tree_start[0][0])
move = minimax(game_tree_start, 0, 0, max_depth, True)[1]
#print(move)


while True:
    if not move.children:
        break
    rock_buffer = move.rocks
    move = minimax(game_tree_start, levels, move.node_id, max_depth, True)[1]
    #if levels % 2 == 0:
    #    print("P1 takes", rock_buffer - move.rocks, " and moves =")
    #else:
    #    print("P2 takes", rock_buffer - move.rocks, "and moves =")
    #print(move)
    levels += 1